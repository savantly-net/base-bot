import logging
import pickle
from pathlib import Path
from typing import Optional

from langchain.vectorstores import VectorStore

from . import config
from .document_loader import get_document_loader
from .ingest import ingest_docs

vectorstore: Optional[VectorStore] = None
vectorstore_variants = config.VECTORSTORE_VARIANTS


def _load_vectorstore(variant: str) -> VectorStore:
    logging.info("loading pickled vectorstore...")
    logging.info(f"variant: {variant if variant else 'default'}")

    vectorstore_path = config.VECTORSTORE_PATH
    
    if variant and variant in vectorstore_variants:
        vectorstore_path = f"{config.VECTORSTORE_PATH}.{variant}"

    if not Path(vectorstore_path).exists():
        if config.VECTORSTORE_CREATE_IF_MISSING:
            logging.info(f"{vectorstore_path} does not exist, creating from docs")

            ingest_docs(
                document_loader=get_document_loader(config.DOCS_PATH),
                vectorstore_path=vectorstore_path,
            )
        else:
            raise ValueError(
                f"{vectorstore_path} does not exist, please run ingest.py first"
            )
    with open(vectorstore_path, "rb") as f:
        vstore = pickle.load(f)
        logging.info("loaded vectorstore")
        return vstore


def get_vectorstore(variant = "") -> VectorStore:
    global vectorstore
    if vectorstore is None:
        vectorstore = _load_vectorstore(variant)
    return vectorstore
