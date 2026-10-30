from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

)
texts = [
    "Hello this is me",
    "Hello your name is WWhat",
    "And you all are very Happy"
]

vector = embedding.embed_documents(texts)
print(vector)