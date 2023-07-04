import pickle

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

from langchain.document_loaders import DirectoryLoader
import config


def ingest_docs():
    docs_dir = "./data/docs"
    print("Loading documents from", docs_dir)
    loader = DirectoryLoader(docs_dir, recursive=True)
    documents = loader.load()

    print("Loaded {} documents".format(len(documents)))

    # split documents into chunks
    chunk_size = config.INGEST_CHUNK_SIZE
    chunk_overlap = config.INGEST_CHUNK_OVERLAP
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    print("Splitting documents into chunks. Chunk size: {}, overlap: {}".format(chunk_size, chunk_overlap))
    documents = text_splitter.split_documents(documents)

    # use OpenAIEmbeddings to embed documents - requires OPENAI_API_KEY set in ENV
    embeddings = OpenAIEmbeddings()

    print("Embedding documents. This may take a while...")
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    vectorstore_path = config.VECTORSTORE_PATH
    print("Saving vectorstore to", vectorstore_path)
    with open(vectorstore_path, "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
