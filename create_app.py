import uvicorn
from fastapi import FastAPI

from web.containers.Container import UserControllerContainer
from web.views import routers
from uvicorn import run


def create_app() -> FastAPI:
    container = UserControllerContainer()
    db = container.database()
    app = FastAPI()

    app.container = container
    for router in routers:
        app.include_router(router)
    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run("create_app:app", host="127.0.0.1", port=8000)
