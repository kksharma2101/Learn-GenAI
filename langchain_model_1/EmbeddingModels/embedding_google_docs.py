from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-exp-03-07",
    dimensions=32
    )

document = [
    "Lucknow is capital of uttar pradesh",
    "Delhi is the UT of india",
    "Modi is the PM of india"
]

# res = embedding.embed_query("Uttar Pradesh is state of the india")
res = embedding.embed_documents(document)

print(str(res))