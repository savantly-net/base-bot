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
