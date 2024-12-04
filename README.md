# CrewAI Hierarchical Tutorial

## Overview
This repository hosts the updated CrewAI tutorial, showcasing advanced AI-powered automation through hierarchical, asynchronous tasks with callbacks and predefined expected outputs. It is designed to illustrate an enhanced workflow for building AI-driven newsletter automation tools.

## Features
- **Hierarchical Task Management:** Leverage the power of structured task execution to maintain a clean and scalable codebase.
- **Asynchronous Tasks:** Improve performance with non-blocking operations, allowing tasks to run concurrently.
- **Callbacks:** Ensure that each task can trigger subsequent actions upon completion, enabling a reactive task flow.
- **Expected Outputs:** Define the anticipated results for each task, streamlining debugging and ensuring quality control.

## Installation
To get started with the CrewAI Hierarchical Tutorial, clone the repository and install the necessary dependencies.

```
git clone https://github.com/your-github-username/crewai-hierarchical-tutorial.git
cd crewai-hierarchical-tutorial
pip install -r requirements.txt
```

## Usage
To run the CrewAI tutorial, execute the main script after setting up your environment variables and configuration.

``` 
python main.py
```

## Structure
main.py: The entry point script that initializes the agents and tasks, and forms the AI crew.

agents.py: Defines various agents like the editor, news fetcher, news analyzer, and newsletter compiler.

tasks.py: Contains the task definitions that are used by the agents to perform specific operations.

file_io.py: Manages file input/output operations, crucial for handling the async flow of data.


Crew Formation
The crew is composed of multiple agents and tasks orchestrated to perform complex newsletter automation.

```
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager=lm=OpenAIGPT4,
    verbose=2
)
```
## Contributing
Contributions to the CrewAI Hierarchical Tutorial are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## Questions & Support
For questions and support, please open an issue in the repository, and we will be happy to assist you.
