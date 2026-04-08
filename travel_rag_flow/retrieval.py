import subprocess
import sys
import os
from promptflow.core import tool


@tool
def retrieval(question: str) -> str:
    # ✅ Install dependency if missing (inside function)
    try:
        from azure.search.documents import SearchClient
        from azure.core.credentials import AzureKeyCredential
    except ImportError:
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "azure-search-documents",
            "azure-core"
        ])
        from azure.search.documents import SearchClient
        from azure.core.credentials import AzureKeyCredential

    search_endpoint = os.environ.get("AZURE_SEARCH_ENDPOINT")
    search_key = os.environ.get("AZURE_SEARCH_KEY")
    index_name = os.environ.get("AZURE_SEARCH_INDEX", "travel-index")

    if not search_endpoint or not search_key:
        return "Azure Search is not configured properly."

    try:
        client = SearchClient(
            endpoint=search_endpoint,
            index_name=index_name,
            credential=AzureKeyCredential(search_key)
        )

        results = client.search(search_text=question, top=3)

        context = ""
        for result in results:
            result_dict = dict(result)

            for field in ["content", "text", "chunk", "description"]:
                value = result_dict.get(field)
                if value:
                    context += value + "\n\n"
                    break

        return context or f"No relevant context found for: {question}"

    except Exception as e:
        return f"Search error: {str(e)}"