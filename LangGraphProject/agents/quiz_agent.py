from state import State

def quiz_agent(state):
    word = state["word"]

    return {
        "quiz": f"'{word}'의 의미는 무엇인가요?"
    }