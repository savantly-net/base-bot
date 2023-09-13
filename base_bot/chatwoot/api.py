import logging

import requests
from fastapi import APIRouter
from langchain.callbacks.base import BaseCallbackHandler

import base_bot.config as cfg
from base_bot.query_data import get_chain
from base_bot.vectorstore import get_vectorstore

from .webhook_payload import Root as ChatwootWebhookPayload

router = APIRouter()


def send_to_chatwoot(account_id: str, conversation_id: str, message: str):
    data = {"content": message}
    url = f"{cfg.CHATWOOT_URL}/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json; charset=utf-8",
        "api_access_token": f"{cfg.CHATWOOT_BOT_TOKEN}",
    }

    r = requests.post(url=url, json=data, headers=headers)
    return r.json()


@router.post("/bot/{chat_variant:str}")
async def bot(payload: ChatwootWebhookPayload, chat_variant: str = ""):
    logging.info(f"received payload: {payload}")
    chatwoot_msg = "None"
    conversation = payload.conversation.id
    account = payload.account.id

    if payload.message_type == "incoming":
        ai_msg = await inference(payload, chat_variant)
        chatwoot_msg = send_to_chatwoot(account_id=account, conversation_id=conversation, message=ai_msg)

    return chatwoot_msg


async def inference(payload: ChatwootWebhookPayload, chat_variant: str):
    callback_handler = BaseCallbackHandler()
    chat_history = []
    vstore = get_vectorstore(chat_variant)
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
