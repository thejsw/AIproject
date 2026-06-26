from fastapi import FastAPI

app = FastAPI()

@app.post("/explain")
async def explain(data: dict):

    return {
        "explanation":
        f"정답은 '{data['word']}' 입니다."
    }