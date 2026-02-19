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

# 1. PLACER ICI : La sélection du modèle (juste après le titre)
provider = st.selectbox("Choisir le fournisseur", ["OpenAI", "Gemini", "Groq"])

if provider == "OpenAI":
    model_name = st.selectbox("Choisir le modèle", ["gpt-4o", "gpt-3.5-turbo"])
    llm = ChatOpenAI(model=model_name, temperature=0)
elif provider == "Gemini":
    model_name = st.selectbox("Choisir le modèle", ["gemini-1.5-flash", "gemini-1.5-pro"])
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)
elif provider == "Groq":
    model_name = st.selectbox("Choisir le modèle", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"])
    llm = ChatGroq(model=model_name, temperature=0)
# initialiser l'historique du chat
if "chat_history" not in st.session_state : 
    st.session_state.chat_history = []

# montrer l'historique du chat 
for message in st.session_state.chat_history :
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Quelle est votre question ?")



if user_prompt : 
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    
    response = llm.invoke(
        [{"role":"system", "content" : "You are a helpful assistant"},*st.session_state.chat_history]
    )
    
    assistant_response = response.content
    
    st.session_state.chat_history.append({"role":"assistant","content": assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)