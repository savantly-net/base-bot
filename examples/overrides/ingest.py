import pickle

from langchain.document_loaders import GoogleDriveLoader, UnstructuredFileIOLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS


GDRIVE_FOLDER_ID = "<use your folder id here>"

INGEST_CHUNK_SIZE = 1000
INGEST_CHUNK_OVERLAP = 200
VECTORSTORE_PATH = './data/stores/vectorstore.pkl'


def ingest_docs():

    loader = GoogleDriveLoader(
        credentials_path='credentials.json',
        token_path='token.json',
        folder_id=GDRIVE_FOLDER_ID,
        #file_types=["document", "sheet"],
        #file_loader_cls=UnstructuredFileIOLoader,
        # Optional: configure whether to recursively fetch files from subfolders. Defaults to False.
        recursive=False,
        file_loader_kwargs={"mode": "elements"},
    )

    documents = loader.load()

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
    vectorstore_path = VECTORSTORE_PATH
    print("Saving vectorstore to", vectorstore_path)
    with open(vectorstore_path, "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
