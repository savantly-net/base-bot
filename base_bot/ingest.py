import pickle

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS


INGEST_CHUNK_SIZE = 1000
INGEST_CHUNK_OVERLAP = 100
VECTORSTORE_PATH = "data/stores/vectorstore.pkl"


def ingest_docs(document_loader, vectorstore_path=VECTORSTORE_PATH):
    documents = document_loader.load()

    print("Loaded {} documents".format(len(documents)))

    # split documents into chunks
    chunk_size = INGEST_CHUNK_SIZE
    chunk_overlap = INGEST_CHUNK_OVERLAP
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    print(
        "Splitting documents into chunks. Chunk size: {}, overlap: {}".format(
            chunk_size, chunk_overlap
        )
    )
    documents = text_splitter.split_documents(documents)

    # use OpenAIEmbeddings to embed documents - requires OPENAI_API_KEY set in ENV
    embeddings = OpenAIEmbeddings()

    print("Embedding documents. This may take a while...")
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    print("Saving vectorstore to", vectorstore_path)
    with open(vectorstore_path, "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    from document_loader import get_document_loader
    ingest_docs(document_loader=get_document_loader())
