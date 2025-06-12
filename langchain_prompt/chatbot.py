from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI;
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-R1-0528", # This model work on HuggingFace API
#     task="text-generation",
#     temperature=0
#     )

# model = ChatHuggingFace(llm=llm)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.header('ChatBot App')

# user_input = st.text_input('You: ')
chat_history = [
    SystemMessage(content= 'You are a helpful assitant')
]
# chat_history.append(user_input)

# if st.button("Send"):
while True:
    user_input = input("you: ")
    chat_history.append(HumanMessage(content= user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI: ", result.content)
    # st.write('AI: ', result.content)
print(chat_history)