import os
from dotenv import load_dotenv

from crewai import Agent, Task, Process, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI  # Alternative LLM option
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Choose your LLM - use OpenAI as a backup if Groq fails
try:
    # Attempt to use Groq first
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="groq/llama-3.1-70b-versatile",
        temperature=0.7
    )

except Exception as e:
    print("Groq LLM initialization failed. Falling back to OpenAI.")
    # Fallback to OpenAI if Groq fails
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",
        temperature=0.7
    )

# Create search tool using CrewAI's SerperDevTool
search_tool = SerperDevTool()

# Define Agents
explorer = Agent(
    role="Senior Researcher",
    goal="Find and explore the most exciting projects and companies in the ai and machine learning space in 2024",
    backstory="""You are an Expert strategist that knows how to spot emerging trends and companies in AI, tech and machine learning. 
    You're great at finding interesting, exciting projects on LocalLLama subreddit. You turn scraped data into detailed reports with names
    of most exciting projects and companies in the ai/ml world. ONLY use scraped data from the internet for the report.
    """,
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

writer = Agent(
    role="Senior Technical Writer",
    goal="Write engaging and interesting blog post about latest AI projects using simple, layman vocabulary",
    backstory="""You are an Expert Writer on technical innovation, especially in the field of AI and machine learning. You know how to write in 
    engaging, interesting but simple, straightforward and concise manner. You know how to present complicated technical terms to general audience in a 
    fun way by using layman words. ONLY use scraped data from the internet for the blog.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

critic = Agent(
    role="Expert Writing Critic",
    goal="Provide feedback and criticize blog post drafts. Make sure that the tone and writing style is compelling, simple and concise",
    backstory="""You are an Expert at providing feedback to technical writers. You can tell when a blog text isn't concise,
    simple or engaging enough. You know how to provide helpful feedback that can improve any text. You know how to make sure that text 
    stays technical and insightful by using layman terms.
    """,
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# Define Tasks with expected_output
task_report = Task(
    description="""Use and summarize scraped data from the internet to make a detailed report on the latest rising projects in AI. Use ONLY 
    scraped data to generate the report. Your final answer MUST be a full analysis report, text only, ignore any code or anything that 
    isn't text. The report has to have bullet points and with 5-10 exciting new AI projects and tools. Write names of every tool and project. 
    Each bullet point MUST contain 3 sentences that refer to one specific ai company, product, model or anything you found on the internet.  
    """,
    expected_output="""A comprehensive markdown report with:
    - 5-10 bullet points
    - Each point covering a unique AI project or tool
    - 3 descriptive sentences per point
    - Focus on latest innovations in AI
    """,
    agent=explorer,
    llm=llm
)

task_blog = Task(
    description="""Write a blog article with text only and with a short but impactful headline and at least 10 paragraphs. Blog should summarize 
    the report on latest ai tools found on localLLama subreddit. Style and tone should be compelling and concise, fun, technical but also use 
    layman words for the general public. Name specific new, exciting projects, apps and companies in AI world. Don't 
    write "**Paragraph [number of the paragraph]:**", instead start the new paragraph in a new line. Write names of projects and tools in BOLD.
    ALWAYS include links to projects/tools/research papers. ONLY include information from LocalLLAma.
    """,
    expected_output="""A markdown-formatted blog post with:
    - Engaging headline
    - At least 10 paragraphs
    - Bold project/tool names
    - Links to projects/research
    - Conversational yet informative tone
    """,
    agent=writer,
    llm=llm
)

task_critique = Task(
    description="""Review the blog post draft. Ensure it meets the following criteria:
    - Compelling and concise writing
    - Technical accuracy
    - Engaging for general audience
    - Proper markdown formatting
    - Correct use of links and bold formatting
    """,
    expected_output="""A critique report with:
    - Specific feedback points
    - Suggestions for improvement
    - Validation of blog post quality
    - Recommendation for final edits
    """,
    context=[task_blog],
    agent=critic,
    llm=llm
)

# Create Crew
crew = Crew(
    agents=[explorer, writer, critic],
    tasks=[task_report, task_blog, task_critique],
    verbose=True,  # Changed from 2 to True
    process=Process.hierarchical,
    manager_llm=llm
)

# Kickoff the research and writing process
result = crew.kickoff()

# Print the final result
print("######################")
print(result)