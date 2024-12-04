# search_tools.py
import os

from dotenv import load_dotenv


from langchain.agents import Tool

from langchain_community.utilities import GoogleSerperAPIWrapper
# Load environment variables from .env file
load_dotenv()
os.environ['SERPAPI_API_KEY'] = os.getenv('SERPER_API_KEY')
class SearchTool:
    
    def __init__(self,search = GoogleSerperAPIWrapper()):
        self.search = search
    
    def launchSearch(self):
        return Tool(
    name="Scrape google searches",
    func=self.search.run,
    description="useful for when you need to ask the agent to search the internet",
)