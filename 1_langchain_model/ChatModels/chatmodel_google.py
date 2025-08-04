from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

res = chatmodel.invoke("generate a poem on cricket")

print(res.content)