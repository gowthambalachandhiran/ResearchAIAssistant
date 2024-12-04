# llm_agent.py
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage  # Import HumanMessage
# Load the .env file
from dotenv import load_dotenv
load_dotenv()

class LLMAgent:
    def __init__(self):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="groq/llama-3.1-70b-versatile",
            temperature=0.7
        )

    async def generate_text(self, prompt: str) -> str:
        # Wrap prompt in HumanMessage
        response = await self.llm.generate([HumanMessage(content=prompt)])
        return response['content']  # Accessing content from response dictionary