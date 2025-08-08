from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# loader = TextLoader("../cricket.txt")
# docs = loader.lazy_load()
# print(docs)

docs = """The leather sphere, a crimson gleam,
Awaiting fate, a silent dream.
The willow waits, a polished grace,
To send it soaring through the space.

The bowler runs, a rhythmic stride,
With eyes of hawk, where secrets hide.
He hurls the ball, a twisting dart,
To break the stumps and pierce the heart.

The batsman stands, a watchful gaze,
A fortress built through sun-drenched days.
He reads the flight, the subtle spin,
And chooses where the game to win."""

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(docs)

print(texts)