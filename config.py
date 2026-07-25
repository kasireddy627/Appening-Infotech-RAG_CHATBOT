import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

PDF_PATH = "data/Ebook-Agentic-AI.pdf"

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
PINECONE_HOST = os.getenv("PINECONE_HOST")

# Validate required variables
required_variables = {
    "GEMINI_API_KEY": GEMINI_API_KEY,
    "PINECONE_API_KEY": PINECONE_API_KEY,
    "PINECONE_INDEX_NAME": PINECONE_INDEX_NAME,
    "PINECONE_HOST": PINECONE_HOST,
}

missing = [key for key, value in required_variables.items() if not value]

if missing:
    raise ValueError(
        f"Missing environment variables: {', '.join(missing)}"
    )