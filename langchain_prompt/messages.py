from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# this is the store chat history
message = [
    SystemMessage(content= 'You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(message)

message.append(AIMessage(content= result.content))

print(message)