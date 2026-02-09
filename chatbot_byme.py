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
    
    # 2. On définit le modèle selon ce que l'utilisateur a écrit
    if "groq" in user_prompt.lower():
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    elif "gemini" in user_prompt.lower():
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    else:
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    response = llm.invoke(
        [{"role":"system", "content" : "You are a helpful assistant"},*st.session_state.chat_history]
    )
    
    assistant_response = response.content
    
    st.session_state.chat_history.append({"role":"assistant","content": assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)