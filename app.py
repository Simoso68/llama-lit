import streamlit as st
import ollama as ol

st.set_page_config("Llama-Lit", "🦙")

class Message():
    def __init__(self, name, content) -> None:
        self.name = name
        self.content = content

def new_chat_message(message: Message):
    if message.name == "ai":
        AVATAR = "https://ollama.com/public/apple-touch-icon.png"
    else:
        AVATAR = None

    with st.chat_message(message.name, avatar=AVATAR):
        st.write(message.content.replace("<", "&#60;").replace(">", "&#62;").replace("\n", "<br>"), unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    new_chat_message(msg)


USER_INPUT = st.chat_input("Ask llama ...")

if USER_INPUT:
    AI_MESSAGES = []
    for msg in st.session_state.messages:
        AI_MESSAGES.append({"role": msg.name, "content": msg.content})
    AI_MESSAGES.append({"role": "user", "content": USER_INPUT})
    new_chat_message(Message("user", USER_INPUT))
    st.session_state.messages.append(Message("user", USER_INPUT))
    AI_STREAM = ol.chat(model=ol.list()["models"][0]["name"], messages=AI_MESSAGES, stream=True)
    st.session_state.response = ""
    RESPONSE_BODY = st.empty()
    with st.chat_message("ai", avatar="https://ollama.com/public/apple-touch-icon.png"):
        for chunk in AI_STREAM:
            st.session_state.response += chunk["message"]["content"]
            RESPONSE_BODY.write(st.session_state.response)
    st.session_state.messages.append(Message("ai", st.session_state.response))
    st.rerun()