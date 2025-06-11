from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI;
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-R1-0528", # This model work on HuggingFace API
#     task="text-generation",
#     temperature=0
#     )

# model = ChatHuggingFace(llm=llm)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.header('ChatBot App')

user_input = st.text_input('You: ')

while True:
    if st.button("Send", key="chat_send_button"):
    # user_input = input("you: ")
        if user_input == "exit":
            st.stop()
            break
    result = model.invoke(user_input)
    # print("AI: ", result.content)
    st.write('AI: ', result.content)