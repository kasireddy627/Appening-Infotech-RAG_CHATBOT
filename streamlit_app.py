import streamlit as st
from graph import graph

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Agentic AI RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "retrieved_chunks" not in st.session_state:
    st.session_state.retrieved_chunks = []

if "scores" not in st.session_state:
    st.session_state.scores = []

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("📘 Knowledge Base")

    st.success("Ebook-Agentic-AI.pdf")

    st.divider()

    st.subheader("Technology")

    st.write("🤖 **LLM**")
    st.caption("Gemini 2.5 Flash")

    st.write("📦 **Embedding**")
    st.caption("Gemini Embedding 001")

    st.write("🗂 **Vector DB**")
    st.caption("Pinecone")

    st.write("🧠 **Workflow**")
    st.caption("LangGraph")

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.session_state.retrieved_chunks = []
        st.session_state.scores = []

        st.rerun()

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("📄 Agentic AI RAG Chatbot")

st.caption(
    "LangGraph • Gemini • Pinecone • Streamlit"
)

st.success("🟢 Knowledge Base Ready")

st.divider()

# ---------------------------------------------------
# Previous Chat
# ---------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------

question = st.chat_input(
    "Ask anything about Agentic AI..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = graph.invoke(
                {
                    "question": question
                }
            )

            answer = result["answer"]

            chunks = result["retrieved_chunks"]

            scores = result["scores"]

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.retrieved_chunks = chunks

    st.session_state.scores = scores

# ---------------------------------------------------
# Retrieved Context
# ---------------------------------------------------

if st.session_state.retrieved_chunks:

    st.divider()

    st.subheader("📚 Retrieved Context")

    for i, (chunk, score) in enumerate(
        zip(
            st.session_state.retrieved_chunks,
            st.session_state.scores
        ),
        start=1
    ):

        with st.expander(
            f"Chunk {i}  •  Similarity Score : {score:.4f}"
        ):

            st.markdown(chunk)

# ---------------------------------------------------
# Retrieval Statistics
# ---------------------------------------------------

if st.session_state.scores:

    st.divider()

    st.subheader("📊 Retrieval Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Retrieved Chunks",
        len(st.session_state.scores)
    )

    col2.metric(
        "Highest Score",
        f"{max(st.session_state.scores):.4f}"
    )

    col3.metric(
        "Average Score",
        f"{sum(st.session_state.scores)/len(st.session_state.scores):.4f}"
    )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.caption(
    "Built using LangGraph • Google Gemini • Pinecone • Streamlit"
)