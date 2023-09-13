import importlib
import logging

from langchain.vectorstores import VectorStore

from base_bot.vectorstores.provider import VectorStoreProvider

from . import config

mod_package = config.VECTORSTORE_PACKAGE
mod_class = config.VECTORSTORE_IMPLEMENTATION
default_variant = config.VECTORSTORE_DEFAULT_VARIANT


# Dynamically import the selected implementation
try:
    logging.info(f"importing module {mod_package}")
    vector_store_module = importlib.import_module(mod_package)

    logging.info(f"importing class {mod_class} from module {mod_package}")
    VectorStoreImplementation = getattr(vector_store_module, mod_class)
except ImportError as err:
    logging.error(f"Error: {err}")
    exit(1)

# Instantiate the selected implementation
vector_store_provider: VectorStoreProvider = VectorStoreImplementation()


def get_vectorstore(variant=default_variant) -> VectorStore:
    global vector_store_provider
    return vector_store_provider.get_vectorstore(variant)
