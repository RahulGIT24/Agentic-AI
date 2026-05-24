from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

import os
import asyncio

os.environ['GROQ_API_KEY'] = os.getenv('LLM_API')

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"uv",
                'args':["run","mathserver.py"],
                "transport":"stdio"
            },
            "weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable-http"
            },
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model='llama-3.3-70b-versatile')
    agent = create_react_agent(model,tools)
    math_response = await agent.ainvoke({
        "messages":[{"role":"user","content":"What is 3 + 5?"}]
    })
    print("Math Response: ",math_response['messages'][-1].content)

asyncio.run(main=main())