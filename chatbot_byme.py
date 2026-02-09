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

if user_prompt : 
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})
    
    if user_prompt.lower().split() == "groq":
        llm = ChatGroq(
            model = "llama-3.3-70b-versatile",
            temperature = 0.0,
        )
    elif user_prompt.lower().split() == "genai":
        llm = ChatGroq(
            model = 'gemini-2.5-flash-lite',
            temperature = 0.0,
        )
    elif user_prompt.lower().split() == "openai":
        llm = ChatGroq(
            model = "gpt-3.5-turbo",
            temperature = 0.0,
        )
    
    response = llm.invoke(
        input({"role":"system", "content" : "You are a helpful assistant"})
    )
    
    assistant_response = response.content
    
    st.session_state.chat_history.append({"role":"system","content": assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)