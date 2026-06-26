from fastapi import FastAPI

app = FastAPI()

@app.post("/quiz")
async def create_quiz(data: dict):

    word = data["word"]

    return {
        "quiz": f"'{word}'의 의미는 무엇인가요?"
    }