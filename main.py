from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = 'data/books'

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob='*.md')
    documents = loader.load()
    return documents

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 500,
    length_function = len,
    add_start_index = True,
)

if __name__ == '__main__':
    documents = load_documents()
    chunks = text_splitter.split_documents(documents)
    print(chunks[0])