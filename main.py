# main.py
from crewai import Crew, Process
from langchain_groq import ChatGroq
from agents import CreateAgent
from tasks import TaskCreater
from file_io import save_markdown
from dotenv import load_dotenv
import os

from langchain.agents import Tool
from tools.search_tools import SearchTool
# Load environment variables from .env file
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
# to get your api key for free, visit and signup: https://serper.dev/
os.environ["SERPER_API_KEY"] = os.getenv('SERPER_API_KEY')
# Initialize the Groq language model
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="groq/llama-3.1-70b-versatile",
    temperature=0.7
)



search = GoogleSerperAPIWrapper()

search_tool = Tool(
    name="Scrape google searches",
    func=search.run,
    description="useful for when you need to ask the agent to search the internet",
)


agent = CreateAgent()

explorer_agent = agent.explorer(search_tool)
writer_agent = agent.writer()
critic = agent.critic()


task = TaskCreater()

explorer_task = task.explorerTask(explorer_agent)
writer_task = task.writerTask(writer_agent)
critic_task = task.criticTask(critic)

crew = Crew(agents=[explorer_agent,writer_agent,critic],
            tasks=[explorer_task,writer_task,critic_task],
            process=Process.hierarchical,
            manager_llm=llm,
            verbose=2)

    # Kick off the crew's work
print("Kick-off crew")
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)
