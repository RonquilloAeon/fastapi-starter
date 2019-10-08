from starlette.requests import Request
from tortoise.transactions import in_transaction

from main import app


@app.middleware('http')
async def db_middleware(request: Request, call_next):
    async with in_transaction():
        return await call_next(request)
