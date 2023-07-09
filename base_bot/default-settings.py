import os

PROJECT_DIRECTORY = f"{os.path.dirname(os.path.realpath(__file__))}/.."

DOCS_PATH = f"{PROJECT_DIRECTORY}/data/docs"

REPHRASE_PROMPT_PATH = f"{PROJECT_DIRECTORY}/data/prompts/condense_question.txt"
QA_PROMPT_PATH = f"{PROJECT_DIRECTORY}/data/prompts/question_answer.txt"

VECTORSTORE_CREATE_IF_MISSING = True
VECTORSTORE_PATH = f"{PROJECT_DIRECTORY}/data/stores/vectorstore.pkl"

INGEST_CHUNK_SIZE = 1000
INGEST_CHUNK_OVERLAP = 200

LOGGING_LEVEL = "DEBUG"

TRACING = True

TEMPLATES_DIR = f"{PROJECT_DIRECTORY}/templates"