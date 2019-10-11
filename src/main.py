from fastapi import FastAPI

import db
from config import config
from core.middleware import DBMiddleware
from views import messages as message_views


def create_app(config):
    app = FastAPI(version=config.API_DEFAULT_VERSION, api_versioning={'header_name': config.API_VERSION_HEADER_NAME})
    app.add_middleware(DBMiddleware)
    app.include_router(message_views.router, prefix='/messages')

    @app.on_event('startup')
    async def startup():
        await db.init(config)

    @app.on_event('shutdown')
    async def shutdown():
        await db.Tortoise.close_connections()

    return app


app = create_app(config)
