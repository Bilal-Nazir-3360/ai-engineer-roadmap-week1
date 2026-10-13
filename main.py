# Venv setup: python -m venv .venv, .\.venv\Scripts\Activate.ps1
# Install packages: pip install requests python-dotenv

import os

import requests
from dotenv import load_dotenv

# dotenv loads settings from the local .env file into environment variables.
load_dotenv()
url = os.getenv("JOKE_API_URL")

try:
    # Make a GET request and wait up to 10 seconds for a response.
    response = requests.get(url, timeout=10)

    # Check the status code before trying to read the JSON response.
    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
    else:
        joke = response.json()
        print("\n--- Random Joke ---")
        if joke["type"] == "single":
            print(joke["joke"])
        else:
            print(joke["setup"])
            print(joke["delivery"])
except requests.exceptions.ConnectionError:
    print("Connection error: check your internet connection.")
except requests.exceptions.Timeout:
    print("Timeout error: the API took too long to respond.")
except requests.exceptions.RequestException as error:
    print(f"Request error: {error}")
