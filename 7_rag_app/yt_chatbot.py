from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


# ========= Step 1a - Indexing (Document Ingestion) ==========
video_id = "HAxhw2tSmww" # only the ID, not full URL
try:
    # If you don’t care which language, this returns the “best” one
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.fetch(video_id, languages=['hi'])
    
    # Flatten it to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(transcript)
    # is iterable
    # for snippet in transcript_list:
    #     print(snippet.text)

    # indexable
    last_snippet = transcript_list[-1]

    # provides a length
    snippet_count = len(transcript_list)

except TranscriptsDisabled:
    print("No captions available for this video.")

# ======== Step 1b - Indexing (Text Splitting) =========
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])