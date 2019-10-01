from fastapi import FastAPI

import db
from config import config

from views import messages_router


def create_app(config):
    app = FastAPI()
    app.include_router(messages_router, prefix='/messages')

    @app.on_event('startup')
    async def startup():
        await db.init(config)

    @app.on_event('shutdown')
    async def shutdown():
        await db.Tortoise.close_connections()

    return app


app = create_app(config)
