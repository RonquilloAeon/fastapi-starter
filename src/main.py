from fastapi import FastAPI

from views import hello_router

app = FastAPI()
app.include_router(hello_router)
