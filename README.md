# Joke API Beginner Project

A simple beginner-level Python project that fetches a random joke from the free [JokeAPI](https://v2.jokeapi.dev/joke/Any).

## Concepts practiced

- Python virtual environments
- `python-dotenv`
- The `requests` library
- GET requests
- JSON parsing
- Exception handling

## Setup

Open PowerShell in this project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install requests python-dotenv
python main.py
```

## Configuration

The `.env` file contains the JokeAPI URL:

```env
JOKE_API_URL=https://v2.jokeapi.dev/joke/Any
```

JokeAPI does not require an API key.

## What the program does

1. Loads the API URL from `.env`.
2. Sends a GET request to JokeAPI.
3. Checks the HTTP status code.
4. Parses the response as JSON.
5. Prints either a one-line joke or a setup and delivery.
6. Handles connection, timeout, and request errors.
