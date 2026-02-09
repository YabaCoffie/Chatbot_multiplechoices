from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(
    page_title = "Chatbot",
    page_icon = "🦾",
    layout = "centered"
)

st.title(" 🤔 Generative AI Chatbot")

# initialiser l'historique du chat
if "chat_history" not in st.session_state : 
    st.session_state.chat_history = []

# montrer l'historique du chat 
for message in st.session_state.chat_history :
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Quel modèle souhaitez vous utiliser ? ")


    