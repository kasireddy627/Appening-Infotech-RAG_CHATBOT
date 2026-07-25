from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not available in the context, say:

"I couldn't find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""
)