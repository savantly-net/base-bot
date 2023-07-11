from langchain.callbacks.base import BaseCallbackManager
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

openai_legacy_models = [
    "text-davinci-003",
    "text-davinci-002",
    "code-davinci-002",
    "davinci",
    "curie",
    "babbage",
    "ada",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
]


def getLLM(
    model: str,
    streaming=False,
    callback_manager: BaseCallbackManager = None,
    verbose: bool = False,
    temperature: float = 0.0,
):
    if model in openai_legacy_models:
        return OpenAI(
            model=model,
            streaming=streaming,
            callback_manager=callback_manager,
            verbose=verbose,
            temperature=temperature,
        )
    else:
        return ChatOpenAI(
            model=model,
            streaming=streaming,
            callback_manager=callback_manager,
            verbose=verbose,
            temperature=temperature,
        )
