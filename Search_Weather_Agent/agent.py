from dotenv import load_dotenv
load_dotenv()
import os
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tool import ALL_TOOLS
from langgraph.checkpoint import InMemorySaver

MODEL =os.getenv("MODEL")

def get_agent():
     "Get Agent with google search and weather search abilities"
     return create_agent(
          model=ChatGroq(model=MODEL),
          tools= ALL_TOOLS,
           system_prompt=(
            "You are a research assistant with google search and weather tools.\n"
            "Use 'google_search' for quick search on google"
            "for deep research that may take several minutes."
            "If user is looking for weather details like temperature, humidity or any other details"
            "then call the 'weather_tool' to get the real time weather data"
        ),
        checkpointer = InMemorySaver()

    
     )


# agent = get_agent()
# while True:
#      query = input("User: ")
#      if query == "exit":
#           break

#      res = agent.invoke({"messages": [{"role":"user", "content":query}]})
#      ans = res["messages"][-1].content
#      print("AI: ", ans)

