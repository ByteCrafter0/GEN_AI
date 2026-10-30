from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions = 65
)
texts = [
    "Hello this is me",
    "Hello your name is WWhat",
    "And you all are very Happy"
]
vector = embeddings.embed_documents(texts)
print(vector)