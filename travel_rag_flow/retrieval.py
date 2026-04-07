from promptflow.core import tool

@tool
def retrieval(question: str) -> str:
    return f"Sample policy context related to: {question}"