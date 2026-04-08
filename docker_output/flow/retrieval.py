from promptflow.core import tool
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

@tool
def retrieval(question: str) -> str:
    search_endpoint = os.environ.get("AZURE_SEARCH_ENDPOINT")
    search_key = os.environ.get("AZURE_SEARCH_KEY")
    index_name = os.environ.get("AZURE_SEARCH_INDEX", "travel-index")

    client = SearchClient(
        endpoint=search_endpoint,
        index_name=index_name,
        credential=AzureKeyCredential(search_key)
    )

    results = client.search(search_text=question, top=3)
    
    context = ""
    for result in results:
        for field in ["content", "text", "chunk", "description"]:
            if field in result and result[field]:
                context += result[field] + "\n\n"
                break

    return context if context else f"No relevant context found for: {question}"