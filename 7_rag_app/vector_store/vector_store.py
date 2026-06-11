# What are vector store?
#  A vector store is a system designed to store and retrieve data represented as numerical vectors.

# ----- There are 4 key features -------
#  Storage 
#  Similarity Search
#  Indexing
#  CRUD Operations

#  ------ Use Cases ------
# Semantic Search
# RAG
# Recommender Systems
# Image/Multimedia Search

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create LangChain documents for IPL players

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )


docs = [doc1, doc2, doc3, doc4, doc5]


vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

# add documents
vector_store.add_documents(docs)

# view documents
vector_store.get(include=['embeddings','documents', 'metadatas'])

# search documents
vector_store.similarity_search(
    query='Who among these are a bowler?',
    k=2
)

# search with similarity score
vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=2
)

# meta-data filtering
vector_store.similarity_search_with_score(
    query="",
    filter={"team": "Chennai Super Kings"}
)

# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)

vector_store.update_document(document_id='enter_document_id', document=updated_doc1)

# view documents
vector_store.get(include=['embeddings','documents', 'metadatas'])

# delete document
vector_store.delete(ids=['09a39dc6-3ba6-4ea7-927e-fdda591da5e4'])

# view documents
vector_store.get(include=['embeddings','documents', 'metadatas'])



# from langchain_huggingface import HuggingFaceEmbeddings  # Changed import
# from langchain_chroma import Chroma
# from langchain_core.documents import Document
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Note: Hugging Face embeddings don't require an API key for local models
# # (No OPENAI_API_KEY check needed)

# # Initialize Hugging Face embeddings instead of OpenAI
# # Using the popular all-MiniLM-L6-v2 model - works well for semantic search [citation:1][citation:4]
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2",  # Free, open-source model
#     model_kwargs={'device': 'cpu'},  # Use 'cuda' if you have GPU
#     encode_kwargs={'normalize_embeddings': True}  # Optional: normalize for similarity search
# )

# # Create LangChain documents for IPL players (same as before)
# doc1 = Document(
#     page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
#     metadata={"team": "Royal Challengers Bangalore"}
# )
# doc2 = Document(
#     page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
#     metadata={"team": "Mumbai Indians"}
# )
# doc3 = Document(
#     page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
#     metadata={"team": "Chennai Super Kings"}
# )
# doc4 = Document(
#     page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
#     metadata={"team": "Mumbai Indians"}
# )
# doc5 = Document(
#     page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
#     metadata={"team": "Chennai Super Kings"}
# )

# docs = [doc1, doc2, doc3, doc4, doc5]

# # Use the Hugging Face embeddings with Chroma (same API as OpenAI!)
# vector_store = Chroma(
#     embedding_function=embeddings,  # Changed from OpenAIEmbeddings()
#     persist_directory='my_chroma_db',
#     collection_name='sample'
# )

# # Add documents
# vector_store.add_documents(docs)

# # View documents
# result = vector_store.get(include=['documents', 'metadatas'])  # Removed 'embeddings' as it can be large
# print(result)

# # Optional: Test similarity search
# query = "Who is the most successful IPL captain?"
# results = vector_store.similarity_search(query, k=2)
# print("\n Search results for:", query)
# for doc in results:
#     print(f"- {doc.page_content[:100]}... (Team: {doc.metadata['team']})")
