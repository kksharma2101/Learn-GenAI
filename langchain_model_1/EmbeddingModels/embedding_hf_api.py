from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
)

# text = "delhi is capital of india"
document = [
    "Lucknow is capital of uttar pradesh",
    "Delhi is the UT of india",
    "Modi is the PM of india"
]

# vector = embedding.embed_query(text)
vector = embedding.embed_documents(document)

print(str(vector))