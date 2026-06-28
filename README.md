🤖 Mira – Personal AI Assistant (RAG Chatbot)

Personal Chatbot

Student Name

Fabiha Fatima

 Student ID

S2024065068

 Project Title

Personal Chatbot

 Chatbot Name

Mira

 Brief Project Description

Mira is a Retrieval-Augmented Generation (RAG) chatbot that answers questions using a custom knowledge base. It uses ChromaDB for vector storage, HuggingFace embeddings for semantic search, Google Gemini for response generation, and Streamlit for the web interface.

Deployment Link

https://mirachatbot-jcpjds3kqx97ykkg8mlgaa.streamlit.app/


Instructions to Run the Project Locally

1. Clone or download the project repository.
2. Install the required dependencies:

   pip install -r requirements.txt

3. Create a `.env` file in the project folder and add your Google Gemini API key:

   
   GOOGLE_API_KEY=YOUR_API_KEY
   
4. Run the Streamlit application:

   streamlit run app.py
   
5. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your browser.

Note

This project uses the free tier of the Google Gemini API. After a certain number of requests, the API may return a quota exceeded or rate limit error. If this happens, wait until the quota resets or use a new API key/project with available quota.

