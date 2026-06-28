import os
from dotenv import load_dotenv
import streamlit as st

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# ----------------------------
# Streamlit Page
# ----------------------------
st.set_page_config(
    page_title="Mira",
    page_icon="🤖",
    layout="centered"
)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:

    st.title("🤖 Mira")

    st.markdown("---")

    st.subheader("About")

    st.write("""
This chatbot uses:

- LangChain
- Google Gemini
- ChromaDB
- Sentence Transformers
- Streamlit
""")

    st.markdown("---")

    st.subheader("Developer")

    st.write("""
**Fabiha Fatima**

BS Software Engineering
""")

st.title("🤖 Mira")

st.markdown("""
### Your Personal AI Assistant

Welcome! 👋

I can answer questions about:

- 🎓 Education
- 💻 Technical Skills
- 🚀 Projects
- 📚 Experience
- 🌱 Interests
- 🎯 Career Goals

Ask me anything using the chat box below.
""")

# ----------------------------
# Load Embedding Model
# ----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ----------------------------
# Load Chroma Vector Database
# ----------------------------
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)



# ----------------------------
# Create Retriever
# ----------------------------
retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)



# ----------------------------
# Load Gemini LLM
# ----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0.3
)



# ----------------------------
# Prompt Template
# ----------------------------
prompt = ChatPromptTemplate.from_template("""
You are Mira, the personal AI assistant of Fabiha Fatima.

Answer ONLY using the provided context.

If the answer is not available in the context, reply:

"I don't have that information in my personal knowledge base."

Context:
{context}

Question:
{question}
""")


# ----------------------------
# Prompt Template
# ----------------------------
prompt = ChatPromptTemplate.from_template("""
You are Mira, the personal AI assistant of Fabiha Fatima.

Answer ONLY from the provided context.

If the answer is not found in the context, say:

"I don't have that information in my personal knowledge base."

Context:
{context}

Question:
{question}
""")



# ----------------------------
# Create RAG Chain
# ----------------------------
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)



# ----------------------------
# Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


    # Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Chat Input
user_question = st.chat_input("Ask Mira anything...")

if user_question:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    # Get answer from RAG
    answer = rag_chain.invoke(user_question)

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)