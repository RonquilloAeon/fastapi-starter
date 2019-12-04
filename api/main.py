from fastapi import FastAPI

from api.db import get_db
from api.message import views as message_views


def create_app(config):
    app = FastAPI(version=config.api_default_version, api_versioning={'header_name': config.api_version_header})
    app.include_router(message_views.router, prefix='/messages')
    db = get_db()

    @app.on_event("startup")
    async def startup():
        await db.database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await db.database.disconnect()

    return app
