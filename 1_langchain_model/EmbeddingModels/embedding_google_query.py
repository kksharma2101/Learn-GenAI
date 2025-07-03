# we used embedding, text convert to vector for contextual understanding
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    # model="text-embedding-3-small",
    model="models/gemini-embedding-exp-03-07",
    dimensions=50
    )

res = embedding.embed_query("Uttar Pradesh is state of the india")

print(str(res))