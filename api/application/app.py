from fastapi import FastAPI

from api.adapters.orm import database
from api.application.category import views as category_views
from api.application.message import views as message_views
from api.config import Config

# Set up app
config = Config()

app = FastAPI(
    version=config.API_DEFAULT_VERSION,
    api_versioning={"header_name": config.API_VERSION_HEADER},
)
app.include_router(category_views.router, prefix="/categories")
app.include_router(message_views.router, prefix="/messages")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
