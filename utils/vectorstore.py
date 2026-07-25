from pinecone import Pinecone

from config import (
    PINECONE_API_KEY,
    PINECONE_HOST,
    PINECONE_INDEX_NAME,
)


def get_pinecone_index():
    """
    Connect to the existing Pinecone index.
    """

    pc = Pinecone(api_key=PINECONE_API_KEY)

    index = pc.Index(
        name=PINECONE_INDEX_NAME,
        host=PINECONE_HOST,
    )

    return index