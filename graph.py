from typing import TypedDict

from langgraph.graph import StateGraph, END

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from config import GEMINI_API_KEY
from prompts.prompt import RAG_PROMPT
from utils.retrieval import retrieve_documents


class RAGState(TypedDict):
    question: str
    context: str
    answer: str
    retrieved_chunks: list
    scores: list


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0,
)


def retrieve_node(state: RAGState):
    docs = retrieve_documents(state["question"])

    context = "\n\n".join(doc.page_content for doc in docs)

    chunks = [doc.page_content for doc in docs]
    scores = [doc.metadata.get("score", 0.0) for doc in docs]

    return {
        "context": context,
        "retrieved_chunks": chunks,
        "scores": scores,
    }


def generate_node(state: RAGState):
    chain = RAG_PROMPT | llm | StrOutputParser()

    answer = chain.invoke(
        {
            "context": state["context"],
            "question": state["question"],
        }
    )

    return {
        "answer": answer
    }


builder = StateGraph(RAGState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.set_entry_point("retrieve")

builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()