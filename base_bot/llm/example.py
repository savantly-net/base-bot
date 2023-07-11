import logging

from langchain.callbacks.base import BaseCallbackManager


def getLLM(
    model: str,
    streaming=False,
    callback_manager: BaseCallbackManager = None,
    verbose: bool = False,
    temperature: float = 0.0,
):
    raise Exception("this is just an example on how to override the getLLM function")
