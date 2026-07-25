from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    """
    Load a PDF and return LangChain Document objects.
    """

    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_file}")

    loader = PyPDFLoader(str(pdf_file))
    documents = loader.load()

    return documents