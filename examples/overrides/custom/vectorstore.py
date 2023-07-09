import logging
import pickle
from pathlib import Path
from typing import Optional

from langchain.vectorstores import VectorStore

from . import config
from ..ingest import ingest_docs

vectorstore: Optional[VectorStore] = None
vectorstore_path = config.VECTORSTORE_PATH


def _load_vectorstore() -> VectorStore:
    logging.info("loading vectorstore")
    if not Path(vectorstore_path).exists():
        if config.VECTORSTORE_CREATE_IF_MISSING:
            logging.info(f"{vectorstore_path} does not exist, creating from docs")

            ingest_docs()
        else:
            raise ValueError(
                f"{vectorstore_path} does not exist, please run ingest.py first"
            )
    with open(vectorstore_path, "rb") as f:
        vstore = pickle.load(f)
        logging.info("loaded vectorstore")
        return vstore


def get_vectorstore() -> VectorStore:
    global vectorstore
    if vectorstore is None:
        vectorstore = _load_vectorstore()
    return vectorstore
