"""Callback handlers used in the app."""
import logging
from typing import Any, Dict, List

from langchain.callbacks.base import AsyncCallbackHandler

from schemas import ChatResponse


class StreamingLLMCallbackHandler(AsyncCallbackHandler):
    """Callback handler for streaming LLM responses."""

    def __init__(self, websocket):
        self.websocket = websocket

    async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        resp = ChatResponse(sender="bot", message=token, type="stream")
        await self.websocket.send_json(resp.dict())


class RephrasedInputGenerationCallbackHandler(AsyncCallbackHandler):
    """Callback handler for rephrased input generation."""

    def __init__(self, websocket):
        self.websocket = websocket

    async def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        logging.info("rephrasing input from prompts %s", prompts)
        """Run when LLM starts running."""
        resp = ChatResponse(
            sender="bot", message="Rephrasing input...", type="info"
        )
        await self.websocket.send_json(resp.dict())
