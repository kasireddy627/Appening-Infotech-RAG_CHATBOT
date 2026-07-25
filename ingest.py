from uuid import uuid4

from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectorstore import get_pinecone_index

# -------------------------------
# Load PDF
# -------------------------------
from config import PDF_PATH

documents = load_pdf(PDF_PATH)

# -------------------------------
# Split into chunks
# -------------------------------
chunks = split_documents(documents)

print(f"Total Chunks : {len(chunks)}")

# -------------------------------
# Embedding Model
# -------------------------------
embeddings = get_embeddings()

# -------------------------------
# Pinecone Index
# -------------------------------
index = get_pinecone_index()

vectors = []

for chunk in chunks:
    embedding = embeddings.embed_query(chunk.page_content)

    vectors.append(
        {
            "id": str(uuid4()),
            "values": embedding,
            "metadata": {
                "text": chunk.page_content,
                "source": chunk.metadata.get("source", ""),
                "page": chunk.metadata.get("page", -1),
            },
        }
    )

# -------------------------------
# Upload to Pinecone
# -------------------------------
print("Uploading vectors...")

batch_size = 20

for i in range(0, len(vectors), batch_size):
    index.upsert(vectors=vectors[i:i + batch_size])

print("Upload Complete!")

stats = index.describe_index_stats()

print("\nIndex Statistics")
print(stats)