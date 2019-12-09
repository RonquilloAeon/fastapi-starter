from fastapi import FastAPI

from api.config import Config
from api.db import database
from api.message import views as message_views

# Set up app
config = Config()

app = FastAPI(
    version=config.API_DEFAULT_VERSION,
    api_versioning={"header_name": config.API_VERSION_HEADER},
)
app.include_router(message_views.router, prefix="/messages")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
