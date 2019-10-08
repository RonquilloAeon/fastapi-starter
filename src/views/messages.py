from fastapi import APIRouter

from models import messages as message_models

router = APIRouter()


@router.get('')
async def read_messages():
    messages = await message_models.Message.all()

    return [{'id': m.id, 'subject': m.subject, 'message': m.message} for m in messages]


@router.post('', response_model=message_models.MessageSchema)
async def write_message(message: message_models.MessageSchema):
    message = await message_models.Message.create(**message.dict(skip_defaults=True))

    # TODO figure out why pydantic blows up so 'message' instance can be returned instead of dict
    return {'id': message.id, 'subject': message.subject, 'message': message.message}
