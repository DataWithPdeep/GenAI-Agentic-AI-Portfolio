from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from tools import *
from dotenv import load_dotenv
from pathlib import Path
import os
from databse import init_db

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
init_db()

##agent = llm , tool, system_prompt, user

print("AGENT.PY STARTED")
print("GROQ KEY FOUND:", bool(os.getenv("GROQ_API_KEY")))

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

all_tools= [create_todo, list_todods, update_todos, delete_todos]

SYSTEM_PROMPT = """You are a smart and friendly Todo Manager AI assistant.

You help users manage their tasks using a database. You can:
  - Create new tasks
  - List / filter tasks by status or priority
  - Update any field of a task (title, description, status, priority, due date)
  - Delete tasks by ID

Guidelines:
- Always confirm what action you took after each tool call.
- When listing todos, present them in a readable table format.
- "mark as done"      → update with status='done'
- "start working on"  → update with status='in_progress'
- "show pending"      → list with status='pending'
- "high priority"     → list with priority='high'
- Be concise and friendly.

Status values:   pending | in_progress | done

Use Status Icons with staus value: 
  pending - 🕣 Pnding 
  in_progress - ⏳ In Progress
  done - ✅ Done
Priority values: low | medium | high
"""

memory = InMemorySaver()
def createAgent():
    agent = create_agent(
        model = llm,
        tools= all_tools,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=memory
        )
    return agent

def call_agent(query:str):
    agent = createAgent()
    res = agent.invoke({
        "messages":[
            {"role":"user", "content": query}]}, 
            {"configurable":{"thread_id":"1"}},
            
            )

    answer =res['messages'][-1].content
    print(answer)

call_agent("List my all the")