import requests

def call_quiz_agent(word: str):

    response = requests.post(
        "http://localhost:8001/quiz",
        json={
            "word": word
        }
    )

    return response.json()