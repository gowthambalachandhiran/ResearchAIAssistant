# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:33:19 2024

@author: gowtham.balachan
"""

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the environment variables
test_env = os.getenv('GROQ_API_KEY')
api_key = os.getenv('SERPER_API_KEY')

# Print the values
print(f"TEST_ENV: {test_env}")
print(f"API_KEY: {api_key}")
