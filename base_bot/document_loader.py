from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.base import BaseLoader
from langchain.document_loaders import PyMuPDFLoader
#from langchain.document_loaders import UnstructuredFileLoader


def get_document_loader(docs_path="data/docs") -> BaseLoader:
    """Return a DocumentLoader instance."""
    print("Loading documents from", docs_path)
    loader = DirectoryLoader(
        path=docs_path,
        recursive=True,
        show_progress=True,
        use_multithreading=True,
        silent_errors=True,
#        loader_cls=UnstructuredFileLoader
    )
    return loader
