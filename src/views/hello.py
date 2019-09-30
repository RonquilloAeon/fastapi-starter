from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_items():
    return {"hello": "world"}
