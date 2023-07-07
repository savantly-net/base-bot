# flake8: noqa
from langchain.prompts.prompt import PromptTemplate
from . import config

REPHRASE_PROMPT = PromptTemplate.from_template(config.REPHRASE_PROMPT)

QA_PROMPT = PromptTemplate(
    template=config.QA_PROMPT, input_variables=["context", "question"]
)
