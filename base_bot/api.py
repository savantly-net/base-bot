import logging

from . import config
from .ui import ui
from .callback import (
    RephrasedInputGenerationCallbackHandler,
    StreamingLLMCallbackHandler,
)
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from .query_data import get_chain
from .schemas import ChatResponse

from .vectorstore import get_vectorstore

templates = Jinja2Templates(directory=config.TEMPLATES_DIR)
router = APIRouter()


@router.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html.j2", {"request": request, "ui": ui})


@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    rephrasing_handler = RephrasedInputGenerationCallbackHandler(websocket)
    stream_handler = StreamingLLMCallbackHandler(websocket)
    chat_history = []
    vstore = get_vectorstore()
    qa_chain = get_chain(vstore, rephrasing_handler, stream_handler)
    # Use the below line instead of the above line to enable tracing
    # Ensure `langchain-server` is running
    # qa_chain = get_chain(vectorstore, question_handler, stream_handler, tracing=True)

    while True:
        try:
            # Receive and send back the client message
            user_input_text = await websocket.receive_text()
            logging.info(f"received message: {user_input_text}")
            resp = ChatResponse(sender="you", message=user_input_text, type="stream")
            await websocket.send_json(resp.dict())

            # Construct a response
            start_resp = ChatResponse(sender="bot", message="", type="start")
            await websocket.send_json(start_resp.dict())

            result = await qa_chain.acall(
                {"question": user_input_text, "chat_history": chat_history}
            )
            logging.debug(f"response: {result}")
            chat_history.append((user_input_text, result["answer"]))

            end_resp = ChatResponse(sender="bot", message="", type="end")
            await websocket.send_json(end_resp.dict())
        except WebSocketDisconnect:
            logging.info("websocket disconnect")
            break
        except Exception as e:
            logging.error(e)
            resp = ChatResponse(
                sender="bot",
                message="Sorry, something went wrong. Try again.",
                type="error",
            )
            await websocket.send_json(resp.dict())
