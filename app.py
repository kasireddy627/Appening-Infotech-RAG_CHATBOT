from fastapi import FastAPI
from pydantic import BaseModel

from graph import graph

app = FastAPI(
    title="RAG Chatbot API",
    description="RAG-based chatbot using LangGraph, Gemini, and Pinecone.",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG Chatbot API is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    retrieved_context = []

    for chunk, score in zip(
        result["retrieved_chunks"],
        result["scores"]
    ):
        retrieved_context.append(
            {
                "score": round(score, 4),
                "chunk": chunk
            }
        )

    return {
        "question": request.question,
        "answer": result["answer"],
        "retrieved_context": retrieved_context
    }