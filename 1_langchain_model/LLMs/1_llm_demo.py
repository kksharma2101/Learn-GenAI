# from langchain_openai import OpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq LLM 
# llm = OpenAI(model='gpt-4.1') # This is the work on paid api key

# Initialize Groq LLM,  This is the Chat Model
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

result = llm.invoke("Who is the prime minister of india")
print(result.content)

# Note - LLMs take a string and return output only string