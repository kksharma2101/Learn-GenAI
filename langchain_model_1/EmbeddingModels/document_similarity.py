from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-exp-03-07",
    dimensions=300
)

document = [
    "Kamal Sharma, known for his aggressive batting and leadership, is one of India's greatest cricketers, holding numerous records in international cricket.",

    "Rohit Sharma, nicknamed 'Hitman,' is famous for his explosive batting and holds the record for the highest individual ODI score (264 runs).",

    "MS Dhoni, India's legendary former captain, led the team to three ICC trophies.",
    
    "Jasprit Bumrah, with his unorthodox bowling action, is considered one of the best fast bowlers in modern cricket, dominating across all formats.",
]

query = "tell me about of rohit sharma"

doc_embedding = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(document[index])
print("similarity score is:", score)