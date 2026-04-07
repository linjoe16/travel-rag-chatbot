from promptflow.core import tool

@tool
def retrieval(question: str) -> str:
    return f"Travel context for: {question}"