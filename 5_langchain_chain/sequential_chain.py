# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"
)
    # "TinyLlama/TinyLlama-1.1B-Chat-v1.0",

model = ChatHuggingFace(llm = llm)
# model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
     input_variables=['text']
)

chain = prompt | model | parser | prompt1 | model | parser

result = chain.invoke({'topic': 'MERN Developer'})

# print(result)

# chain.get_graph().print_ascii()