import os

import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import logging
log = logging.getLogger(__name__)


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# check if params are set
if PINECONE_INDEX_NAME is None:
    raise ValueError("PINECONE_INDEX_NAME not set")
if PINECONE_API_KEY is None:
    raise ValueError("PINECONE_API_KEY not set")
if PINECONE_ENV is None:
    raise ValueError("PINECONE_ENV not set")

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)


INGEST_CHUNK_SIZE = 1000
INGEST_CHUNK_OVERLAP = 0


def ingest_docs(document_loader, namespace="default"):
    """Ingest documents into Pinecone."""
    # check pinecone client is connected
    print("Checking Pinecone connection...")
    pinecone.list_indexes()
    
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
    p = Pinecone.from_existing_index(PINECONE_INDEX_NAME, embeddings, namespace=namespace)
    step = 10
    for i in range(0, len(documents), step):
        p.add_documents(documents[i:min(i+step, len(documents))])
        print(f"Added {i+step} documents")

    #Pinecone.from_documents(documents, embeddings, index_name=PINECONE_INDEX_NAME)
    print("Done!")


if __name__ == "__main__":
    from ..document_loader import get_document_loader
    variant = input("Enter variant name (base-bot): ")
    if variant == "":
        variant = "base-bot"
    docs_path = f"data/docs/private/{variant}"
    print(f"Loading documents from {docs_path}")
    input("Press enter to start ingesting documents...")
    ingest_docs(document_loader=get_document_loader(docs_path=docs_path), namespace=variant)
