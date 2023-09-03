import logging

import base_bot.config as cfg
import requests
from base_bot.query_data import get_chain
from base_bot.vectorstore import get_vectorstore
from fastapi import APIRouter
from langchain.callbacks.base import BaseCallbackHandler

from .webhook_payload import Root as ChatwootWebhookPayload

router = APIRouter()


def send_to_chatwoot(account, conversation, message: str):
    data = {"content": message}
    url = f"{cfg.CHATWOOT_URL}/api/v1/accounts/{account}/conversations/{conversation}/messages"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api_access_token": f"{cfg.CHATWOOT_BOT_TOKEN}",
    }

    r = requests.post(url, json=data, headers=headers)
    return r.json()


@router.post("/langchain")  # type: ignore
async def langchain(payload: ChatwootWebhookPayload):
    chatwoot_msg = "None"
    conversation = payload.conversation.display_id
    account = payload.account.id

    if payload.message_type == "incoming":
        ai_msg = await inference(payload)  # type: ignore
        chatwoot_msg = send_to_chatwoot(account, conversation, ai_msg)

    return chatwoot_msg


async def inference(payload: ChatwootWebhookPayload):
    callback_handler = BaseCallbackHandler()
    chat_history = []
    vstore = get_vectorstore(cfg.CHATWOOT_BOT_VARIANT)
    qa_chain = get_chain(vstore, callback_handler, callback_handler)

    # Receive and send back the client message
    logging.info(f"received payload: {payload}")

    user_input_text = payload.content

    result = await qa_chain.acall(
        {"question": user_input_text, "chat_history": chat_history}
    )
    logging.info(f"response: {result}")
    ai_msg = result["answer"]
    chat_history.append((user_input_text, ai_msg))
    return ai_msg
