"""Main entrypoint for the app."""

from . import vectorstore
from .api import router
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    vectorstore.get_vectorstore()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
