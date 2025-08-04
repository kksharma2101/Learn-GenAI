from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.0-flash")

loader = PyPDFLoader('llm_test.pdf')
docs = loader.load()
# print(docs[0])

prompt = PromptTemplate(
    template="write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

# ====== Another PDF Loaders ======
# - PDFPlumberLoader => PDFs with tables/columns
# - UnstructuredPDFLoader or AmazonTextractLoader => Scanned/image PDFs
# - PyMuPDFLoader => Need layout and image data