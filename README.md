🤖 Mira – Personal AI Assistant (RAG Chatbot)

 Project Overview

Mira is a Retrieval-Augmented Generation (RAG) chatbot developed as a semester project. The chatbot is designed to answer questions about Fabiha Fatima by retrieving relevant information from a custom knowledge base and generating accurate responses using Google's Gemini Large Language Model.

Instead of relying only on the language model, Mira first searches a vector database built from personal documents and then generates responses based on the retrieved context. This improves accuracy and reduces incorrect or fabricated answers.

---

 Features

Personal AI assistant named **Mira**
 nswers questions based on a custom knowledge base
Ues Retrieval-Augmented Generation (RAG)
tres document embeddings in ChromaDB
ses Google's Gemini 2.5 Flash model
nteractive web interface built with Streamlit
Maintains chat history during the session
 Responds with "I don't have that information in my personal knowledge base." when information is unavailable

---

 Technologies Used

 Python
 Streamlit
 LangChain
 Google Gemini API
 ChromaDB
 HuggingFace Sentence Transformers
 dotenv

---

 Project Structure

Mira-RAG/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
├── dataset/
├── chroma_db/
└── RAG.ipynb


---

 How It Works

1. Personal documents are stored inside the **dataset** folder.
2. Documents are loaded and divided into smaller text chunks.
3. Each chunk is converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User questions are converted into embeddings.
6. The retriever finds the most relevant document chunks.
7. Gemini generates an answer using the retrieved context.
8. The response is displayed through the Streamlit interface.

---

 Installation

1. Clone or download the project.
2. Install the required libraries:


pip install -r requirements.txt


3. Create a `.env` file and add your Gemini API key:

GOOGLE_API_KEY=YOUR_API_KEY


4. Run the application:


streamlit run app.py


---

 Example Questions

What is your name?
 Which university do you study at?
 Tell me about your AI Crop Disease project.
 What programming languages do you know?
 What are your interests?
 What are your technical skills?
---

Developer

Name: Fabiha Fatima

Degree:** BS Software Engineering

University:** University of Management and Technology (UMT)



 Future Improvements

 Voice-based interaction
 PDF document support
 Image-based question answering
 Cloud deployment
 Multi-user support

---

📄 License

This project was developed for educational purposes as a university semester project.
