import requests

def call_explanation_agent(word: str):

    response = requests.post(
        "http://localhost:8002/explain",
        json={
            "word": word
        }
    )

    return response.json()