from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv  import load_dotenv

load_dotenv()

loader = PyPDFLoader('../llm_test.pdf')
docs = loader.load()
# print(docs)
text_splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator=""
)

chunks = text_splitter.split_text(docs[0].page_content)

print(chunks)