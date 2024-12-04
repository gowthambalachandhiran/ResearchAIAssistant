# test_search_tool.py
import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def search_internet(query):
    """Useful to search the internet about a given topic and return relevant results."""
    print("Searching the internet...")
    top_result_to_return = 5
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query, "num": top_result_to_return, "tbm": "nws"})
    headers = {
        'X-API-KEY': os.environ['SERPER_API_KEY'],
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    # Check if there is an organic key in the response
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    
    results_json = response.json()
    
    if 'organic' not in results_json or not results_json['organic']:
        return "Sorry, I couldn't find anything about that. There could be an error with your Serper API key."
    
    results = results_json['organic']
    string = []
    
    for result in results[:top_result_to_return]:
        try:
            # Attempt to extract the date
            date = result.get('date', 'Date not available')
            string.append('\n'.join([
                f"Title: {result['title']}",
                f"Link: {result['link']}",
                f"Date: {date}",  # Include the date in the output
                f"Snippet: {result['snippet']}",
                "\n-----------------"
            ]))
        except KeyError:
            continue

    return '\n'.join(string)

if __name__ == "__main__":
    query = "latest AI news"  # You can change this to any other query you want to test
    results = search_internet(query)
    print("Search Results:\n", results)