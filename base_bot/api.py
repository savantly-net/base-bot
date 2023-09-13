from fastapi import APIRouter, Request, WebSocket
from fastapi.templating import Jinja2Templates

from . import api_ws_chat, config
from .ui import ui

templates = Jinja2Templates(directory=config.TEMPLATES_DIR)
router = APIRouter()
default_variant = config.VECTORSTORE_DEFAULT_VARIANT

@router.get("/")
@router.get("/{chat_variant:str}")
async def get(request: Request, chat_variant: str = default_variant):
    return templates.TemplateResponse("index.html.j2", {"request": request, "ui": ui, "chat_variant": chat_variant})


@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
   await api_ws_chat.websocket_endpoint(websocket)

if config.CHATWOOT_ENABLED:
    from .chatwoot import api as chatwoot_api
    router.include_router(chatwoot_api.router, prefix="/chatwoot")