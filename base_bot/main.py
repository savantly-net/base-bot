"""Main entrypoint for the app."""

import logging
import os

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .vectorstore import get_vectorstore
from .api import router
from fastapi import FastAPI, Request, status


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    get_vectorstore()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", 9000))
