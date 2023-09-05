import os

PROJECT_DIRECTORY = f"{os.path.dirname(os.path.realpath(__file__))}/.."

DOCS_PATH = f"{PROJECT_DIRECTORY}/data/docs"


REPHRASE_PROMPT = """
Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:
"""

QA_PROMPT = """
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:
"""

VECTORSTORE_CREATE_IF_MISSING = True
VECTORSTORE_PATH = f"{PROJECT_DIRECTORY}/data/stores/vectorstore.pkl"
VECTORSTORE_VARIANTS = []
VECTORSTORE_PACKAGE = "base_bot.vectorstores.provider_default"
VECTORSTORE_IMPLEMENTATION = "DefaultVectorStore"

INGEST_CHUNK_SIZE = 1000
INGEST_CHUNK_OVERLAP = 100

LOGGING_LEVEL = "DEBUG"

TRACING = True

TEMPLATES_DIR = f"{PROJECT_DIRECTORY}/templates"

LLM_REPRHASING_MODEL = "gpt-3.5-turbo"
LLM_REPHRASING_TEMPERATURE = 0.0
LLM_REPHRASING_VERBOSE = True
LLM_STREAMING_MODEL = "gpt-3.5-turbo"
LLM_STREAMING_TEMPERATURE = 0.1
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


# Chatwoot
CHATWOOT_ENABLED = False
CHATWOOT_URL = "https://chatwoot.com"
CHATWOOT_BOT_TOKEN = ""