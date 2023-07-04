import os

PROJECT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

REPHRASE_PROMPT_PATH = f"{PROJECT_DIRECTORY}/data/prompts/condense_question.txt"
QA_PROMPT_PATH = f"{PROJECT_DIRECTORY}/data/prompts/question_answer.txt"
VECTORSTORE_PATH = f"{PROJECT_DIRECTORY}/data/stores/vectorstore.pkl"

INGEST_CHUNK_SIZE = 1000
INGEST_CHUNK_OVERLAP = 200