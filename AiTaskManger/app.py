from agent import createAgent
import streamlit as st


if "agent" not in st.session_state:
    st.session_state.agent = createAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("AI TASK MANAGER")

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]

    st.chat_message(role).markdown(content)

query = st.chat_input("Manage your task...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    res = st.session_state.agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}},
    )

    answer = res["messages"][-1].content
    st.session_state.messages.append({"role": "ai", "content": answer})
    st.chat_message("ai").markdown(answer)