from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='', # give the file location path
    glob='', # the abstrict and other like that eg. "*.pdf"
    loader_cls=PyPDFLoader()
)

# loader.load() # load the data once
loader.lazy_load() # load the data in chunks