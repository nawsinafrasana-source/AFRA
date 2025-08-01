from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import *

embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")


url=""
api_key=""

question = input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=url,
    api_key=api_key,
    collection_name="bitcoin",
)

response =  qdrant.similarity_search(
    query=question,
    k=5)
# for score in response:
#     print(  score)

prompt = f"""

Question: {question},
context: {response}
Only return the summary based on the provided content.
"""

print(completion_llm(prompt))
# for i in completion_llm(prompt):
#     print(i, end="", flush=True)