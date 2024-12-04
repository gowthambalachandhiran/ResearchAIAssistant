# agents.py
from crewai import Agent
from langchain.tools import Tool
#from tools.search_tools import search_internet  # Import the search function directly

class CreateAgent:
    def explorer(self,search_tool):
        return Agent(
    role="Senior Researcher",
    goal="Find and explore the most exciting projects and companies in the ai and machine learning space in 2024",
    backstory="""You are and Expert strategist that knows how to spot emerging trends and companies in AI, tech and machine learning. 
    You're great at finding interesting, exciting projects on LocalLLama subreddit. You turned scraped data into detailed reports with names
    of most exciting projects an companies in the ai/ml world. ONLY use scraped data from the internet for the report.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
)
    
    def writer(self):
        return Agent(
    role="Senior Technical Writer",
    goal="Write engaging and interesting blog post about latest AI projects using simple, layman vocabulary",
    backstory="""You are an Expert Writer on technical innovation, especially in the field of AI and machine learning. You know how to write in 
    engaging, interesting but simple, straightforward and concise. You know how to present complicated technical terms to general audience in a 
    fun way by using layman words.ONLY use scraped data from the internet for the blog.""",
    verbose=True,
    allow_delegation=True,
)
    
    def critic(self):
        return Agent(
    role="Expert Writing Critic",
    goal="Provide feedback and criticize blog post drafts. Make sure that the tone and writing style is compelling, simple and concise",
    backstory="""You are an Expert at providing feedback to the technical writers. You can tell when a blog text isn't concise,
    simple or engaging enough. You know how to provide helpful feedback that can improve any text. You know how to make sure that text 
    stays technical and insightful by using layman terms.
    """,
    verbose=True,
    allow_delegation=True,
)
