from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

# Chunk + Embed into Chroma.
def build_vectorstore(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
    )
    chunks = splitter.create_documents([text])

    embeddings = OllamaEmbeddings(model=os.getenv("OLLAMA_EMBED_MODEL"))
    vectordb = Chroma(
        collection_name="filtered_web",
        embedding_function=embeddings,
        persist_directory=os.getenv("CHROMA_DIR"),
    )
    vectordb.add_documents(chunks)
    vectordb.persist()
    
    return vectordb