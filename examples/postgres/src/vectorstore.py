import logging
import os
from typing import Optional

import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone, VectorStore

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

vectorstore: Optional[VectorStore] = None


def _load_vectorstore() -> VectorStore:
    logging.info("loading pinecone vectorstore...")
    logging.info("checking pinecone connection...")
    pinecone.list_indexes()
    logging.info("pinecone connection ok")

    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(PINECONE_INDEX_NAME, embeddings)


def get_vectorstore() -> VectorStore:
    global vectorstore
    if vectorstore is None:
        vectorstore = _load_vectorstore()
    return vectorstore
