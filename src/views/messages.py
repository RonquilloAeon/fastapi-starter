from fastapi import APIRouter

from models import Message

router = APIRouter()


@router.get('')
async def read_messages():
    messages = await Message.all()

    return [{'id': m.id, 'subject': m.subject, 'message': m.message} for m in messages]
