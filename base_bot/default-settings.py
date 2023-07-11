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

LLM_REPRHASING_MODEL = "gpt-3.5-turbo"
LLM_REPHRASING_TEMPERATURE = 0.0
LLM_REPHRASING_VERBOSE = True
LLM_STREAMING_MODEL = "gpt-3.5-turbo"
LLM_STREAMING_TEMPERATURE = 0.0
LLM_STREAMING_VERBOSE = True
LLM_MODULE = "openai"

UI_PAGE_TITLE = "Savantly Base Bot"
UI_PAGE_DESCRIPTION = "Savantly Base Bot"
UI_PAGE_FAVICON = "https://savantly.net/img/favicon.png"
UI_SHOW_HEADER = True
UI_HEADER_CENTER = True
UI_HEADER_TITLE = "BASEBOT"
UI_HEADER_LOGO_SRC = "https://savantly.net/img/logo.png"
UI_HEADER_LOGO_ALT = "Savantly Logo"
UI_HEADER_LOGO_HREF = "https://savantly.net"
UI_CHAT_BOT_NAME = "BaseBot"