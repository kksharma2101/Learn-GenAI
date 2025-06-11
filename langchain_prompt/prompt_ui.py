from langchain_google_genai import ChatGoogleGenerativeAI;
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528", # This model work on HuggingFace API
    task="text-generation",
    temperature=1.5
    )

model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

# user_input = st.text_input('Enter your prompt') # This is the static input some time create inhelusion output

paper_input = st.selectbox("Select Research Paper Name",["Attention Is All You Need", "BERT: Pre-training of deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Deffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style",["Begineer-Friendly", "Technical", "Code-Oriented", "Mathematical"])

input_length = st.selectbox("Select Explanation Length", ["Short (1-2 Paragraphs)", "Medium (3-5 Paragraphs)", "Long (detailed explanation)"])

template = load_prompt('../template.json')

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'input_length': input_length
# })

if st.button('Summarise'):
    # result = model.invoke(prompt)
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'input_length': input_length
})
    st.write(result.content)