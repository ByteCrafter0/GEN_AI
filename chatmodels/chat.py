from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from langchain_groq import ChatGroq
model = ChatGroq(model="openai/gpt-oss-120b",temperature=0.9)
response=model.invoke("write a poem about the beauty of mother nature")
print(response.content)
