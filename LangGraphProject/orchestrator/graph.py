from langgraph.graph import StateGraph, END
from state import State

from clients.quiz_client import call_quiz_agent
from clients.explanation_client import call_explanation_agent

# 데이터 구조를 관리할 준비
builder = StateGraph(State)

# 노드 이름과 실행 함수 연결
builder.add_node("quiz", call_quiz_agent)
builder.add_node("explanation", call_explanation_agent)

# 그래프의 시작점 정의
builder.set_entry_point("quiz")

# 그래프의 실행 순서, 종료 조건 정의
builder.add_edge("quiz", "explanation")
builder.add_edge("explanation", END)

# 실제 실행 가능한 객체 제작
graph = builder.compile()

# 실행 시작
result = graph.invoke({
    "word": "study"
})

print(result)