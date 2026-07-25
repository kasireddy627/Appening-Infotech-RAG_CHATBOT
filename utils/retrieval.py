from langchain_core.documents import Document

from utils.embeddings import get_embeddings
from utils.vectorstore import get_pinecone_index


def retrieve_documents(query: str, top_k: int = 5):
    """
    Retrieve the most relevant documents from Pinecone.
    """

    embeddings = get_embeddings()
    index = get_pinecone_index()

    query_embedding = embeddings.embed_query(query)

    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
    )

    documents = []

    for match in results["matches"]:
        documents.append(
            Document(
                page_content=match["metadata"]["text"],
                metadata={
                    "score": match["score"],
                    "source": match["metadata"].get("source", ""),
                    "page": match["metadata"].get("page", -1),
                },
            )
        )

    return documents