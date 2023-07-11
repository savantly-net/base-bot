import logging
import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="SAVANTLY_CHAT",
    settings_files=["base_bot/default-settings.py", "settings.py", ".secrets.py"],
)

# `envvar_prefix` = export envvars with `export SAVANTLY_CHAT_FOO=bar`.
# `settings_files` = Load these files in the order.

# Provide strongly-typed access to settings.
# See https://www.dynaconf.com/ for more information.

DOCS_PATH = settings.DOCS_PATH

# read the contents of the file into a variable
REPHRASE_PROMPT: str = ""
with open(settings.REPHRASE_PROMPT_PATH, "r") as file:
    REPHRASE_PROMPT = file.read()

QA_PROMPT: str = ""
with open(settings.QA_PROMPT_PATH, "r") as file:
    QA_PROMPT = file.read()

VECTORSTORE_PATH = settings.VECTORSTORE_PATH
VECTORSTORE_CREATE_IF_MISSING = settings.VECTORSTORE_CREATE_IF_MISSING

INGEST_CHUNK_SIZE = settings.INGEST_CHUNK_SIZE
INGEST_CHUNK_OVERLAP = settings.INGEST_CHUNK_OVERLAP

logging.basicConfig(level=settings.LOGGING_LEVEL)

os.environ["LANGCHAIN_TRACING"] = str(settings.TRACING)

TEMPLATES_DIR = settings.TEMPLATES_DIR

LLM_REPRHASING_MODEL = settings.LLM_REPRHASING_MODEL
LLM_REPHRASING_TEMPERATURE = settings.LLM_REPHRASING_TEMPERATURE
LLM_REPHRASING_VERBOSE = settings.LLM_REPHRASING_VERBOSE
LLM_STREAMING_MODEL = settings.LLM_STREAMING_MODEL
LLM_STREAMING_TEMPERATURE = settings.LLM_STREAMING_TEMPERATURE
LLM_STREAMING_VERBOSE = settings.LLM_STREAMING_VERBOSE
LLM_MODULE = settings.LLM_MODULE

UI_PAGE_TITLE = settings.UI_PAGE_TITLE
UI_PAGE_DESCRIPTION = settings.UI_PAGE_DESCRIPTION
UI_PAGE_FAVICON = settings.UI_PAGE_FAVICON
UI_SHOW_HEADER = settings.UI_SHOW_HEADER
UI_HEADER_CENTER = settings.UI_HEADER_CENTER
UI_HEADER_TITLE = settings.UI_HEADER_TITLE
UI_HEADER_LOGO_SRC = settings.UI_HEADER_LOGO_SRC
UI_HEADER_LOGO_ALT = settings.UI_HEADER_LOGO_ALT
UI_HEADER_LOGO_HREF = settings.UI_HEADER_LOGO_HREF
UI_CHAT_BOT_NAME = settings.UI_CHAT_BOT_NAME

