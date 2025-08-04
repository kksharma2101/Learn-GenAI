from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")

loader = TextLoader('cricket.txt')

prompt = PromptTemplate(
    template="write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

docs = loader.load()
# print(type(docs[0]))

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))