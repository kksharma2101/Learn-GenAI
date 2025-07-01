from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_output_parser import StrOutputParser

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-R1-0528",
#     task="text-generation"
# )
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

# model = ChatHuggingFace(llm = llm)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)