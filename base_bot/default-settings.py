import os

PROJECT_DIRECTORY = f"{os.path.dirname(os.path.realpath(__file__))}/.."

# read the version from the VERSION file
VERSION = open(f"{PROJECT_DIRECTORY}/VERSION").read().strip()

DOCS_PATH = f"{PROJECT_DIRECTORY}/data/docs"


REPHRASE_PROMPT = """
Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:
"""

QA_PROMPT = """
You are "The Savantly Founder's Digital Persona".
You are answering a question about Savantly and have some of the founder's memories in the context.
Be friendly, kind, inspiring, and eager to provide vivid and thoughtful responses to the user.
You are able to answer most questions about technology.

START CONTEXT BLOCK
${context}
END OF CONTEXT BLOCK

AI will take into account any CONTEXT BLOCK that is provided in a conversation.
If the context does not provide the answer to question, AI will refer the person to contact support@savantly.net for more information.
AI will not apologize for previous responses, but instead will indicated new information was gained.
AI will not be able to answer questions that are not directly related to the context.
Limit the response to 3-5 sentences.
Reply in Markdown format.

Question: {question}
Helpful Answer:
"""

VECTORSTORE_CREATE_IF_MISSING = True
VECTORSTORE_PATH = f"{PROJECT_DIRECTORY}/data/stores/vectorstore.pkl"
VECTORSTORE_VARIANTS = []
VECTORSTORE_DEFAULT_VARIANT = ""
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
UI_SHOW_DISCLAIMER = True
UI_DISCLAIMER_TEXT = """
This is for entertainment purposes only.  
The information provided by this chatbot is not a substitute for professional advice.  
If you have a medical emergency, call your doctor or 911 immediately.  
Do not rely on this chatbot for assistance in regard to your medical needs.  
This chatbot is not designed to diagnose, treat, cure or prevent any disease.  
If you have any concerns or questions about your health, you should always consult with a physician or other health-care professional.  
Do not disregard, avoid or delay obtaining medical or health related advice from your health-care professional because of something you may have read on this chatbot.  
The use of any information provided by this chatbot is solely at your own risk.  
"""


# Chatwoot
CHATWOOT_ENABLED = False
CHATWOOT_URL = "https://chatwoot.com"
CHATWOOT_BOT_TOKEN = ""