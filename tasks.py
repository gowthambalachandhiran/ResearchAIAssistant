from crewai import Task


class TaskCreater:
    
    def explorerTask(self,explorerAgent):
        task_report = Task(
        description="""Use and summarize scraped data from the internet to make a detailed report on the latest rising projects in AI. Use ONLY 
        scraped data to generate the report. Your final answer MUST be a full analysis report, text only, ignore any code or anything that 
        isn't text. The report has to have bullet points and with 5-10 exciting new AI projects and tools. Write names of every tool and project. 
        Each bullet point MUST contain 3 sentences that refer to one specific ai company, product, model or anything you found on the internet.  
        """,
        async_execution=True,
        agent=explorerAgent,
    )
        return task_report
        
        
    def writerTask(self,writerAgent):
        task_blog = Task(
    description="""Write a blog article with text only and with a short but impactful headline and at least 10 paragraphs. Blog should summarize 
    the report on latest ai tools found on localLLama subreddit. Style and tone should be compelling and concise, fun, technical but also use 
    layman words for the general public. Name specific new, exciting projects, apps and companies in AI world. Don't 
    write "**Paragraph [number of the paragraph]:**", instead start the new paragraph in a new line. Write names of projects and tools in BOLD.
    ALWAYS include links to projects/tools/research papers. ONLY include information from LocalLLAma.
    For your Outputs use the following markdown format:
    ```
    ## [Title of post](link to project)
    - Interesting facts
    - Own thoughts on how it connects to the overall theme of the newsletter
    ## [Title of second post](link to project)
    - Interesting facts
    - Own thoughts on how it connects to the overall theme of the newsletter
    ```
    """,
    async_execution=True,
    agent=writerAgent,
)
        return task_blog
    
    def criticTask(self,critiAgent):
        task_critique = Task(
    description="""The Output MUST have the following markdown format:
    ```
    ## [Title of post](link to project)
    - Interesting facts
    - Own thoughts on how it connects to the overall theme of the newsletter
    ## [Title of second post](link to project)
    - Interesting facts
    - Own thoughts on how it connects to the overall theme of the newsletter
    ```
    Make sure that it does and if it doesn't, rewrite it accordingly.
    """,
    agent=critiAgent,
)
        return task_critique