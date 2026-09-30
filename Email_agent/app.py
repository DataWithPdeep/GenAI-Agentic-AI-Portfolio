from agent import get_agent
import streamlit as st




st.subheader("Email Agent")
st.caption("Send email to any email address")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "agent" not in st.session_state:
    st.session_state.agent = get_agent()

for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))
    
query = st.chat_input("Ask anything ....")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    
    res = st.session_state.agent.invoke(
        {"messages": [ {"role":"user", "content":query} ]},
        {"configurable": {"thread_id": "chat_1"}}
        )
    ans = res["messages"][-1].content
    
    st.session_state.messages.append({"role":"ai", "content":ans})
    st.chat_message("ai").markdown(ans)
    
    