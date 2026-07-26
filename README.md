# RAG-based AI Chatbot using LangGraph

A Retrieval-Augmented Generation (RAG) chatbot built using **LangGraph**, **Google Gemini**, **Pinecone**, **FastAPI**, and **Streamlit**. The chatbot answers questions strictly based on the **Agentic AI eBook** by retrieving relevant context from a vector database.

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini
- Pinecone
- FastAPI
- Streamlit

---

## Project Structure

```text
.
├── app.py                 # FastAPI application
├── streamlit_app.py       # Streamlit UI
├── graph.py               # LangGraph workflow
├── ingest.py              # PDF ingestion
├── config.py
├── requirements.txt
├── prompts/
├── utils/
├── data/
└── screenshots/
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kasireddy627/Appening-Infotech-AI-Engineer---Interview-Task.git

cd Appening-Infotech-AI-Engineer---Interview-Task
```

### 2. Create Virtual Environment

**Windows**

```bash
python -m venv rag_venv

rag_venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv rag_venv

source rag_venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
PINECONE_API_KEY=YOUR_API_KEY
PINECONE_INDEX_NAME=YOUR_INDEX_NAME
PINECONE_HOST=YOUR_PINECONE_HOST
```

### 5. Ingest the PDF

```bash
python ingest.py
```

### 6. Start the FastAPI Server

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

### 7. Run the Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## API

### POST `/chat`

Request

```json
{
  "question": "What is Agentic AI?"
}
```

Response

```json
{
  "question": "What is Agentic AI?",
  "answer": "...",
  "retrieved_context": [
    {
      "score": 0.87,
      "chunk": "..."
    }
  ]
}
```

---

## Sample Questions

- What is Agentic AI?
- Explain Agentic AI architecture.
- What are Multi-Agent Systems?
- What is the planning phase?
- How is Agentic AI different from traditional AI?

---

## Author

**Kambalapalle Kasi Reddy**

AI Engineer Internship Assignment – Appening Infotech