from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

llm = ChatGroq(model="openai/gpt-oss-20b")
history = []

for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))

      
st.subheader("🤖 Qna Bot")
query = st.chat_input("Ask anything")
if query:
        st.session_state.messages.append({"role":"user", "content":query})
        st.chat_message("user").markdown(query)

        res =llm.invoke(st.session_state.messages)
        st.session_state.messages.append({"role":"ai","content":res.content})
        st.chat_message("ai").markdown(res.content)

print(st.session_state)