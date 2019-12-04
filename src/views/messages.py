from fastapi import APIRouter
from typing import List

from versioning import version, VersionedRoute
from models import messages as message_models

router = APIRouter(route_class=VersionedRoute)


@router.get('', response_model=List[message_models.MessageSchema])
@version('2019', '10', '09')
async def read_messages():
    return await message_models.Message.objects.all()


@router.get('')
@version('2019', '09', '25')
async def read_messages_old():
    messages = await message_models.Message.objects.all()

    return [{"id": m.id, "subject": m.subject, "message": m.message, "old": True} for m in messages]


@router.post('', response_model=message_models.MessageSchema)
@version('2019', '09', '25')
async def write_message(message: message_models.MessageSchema):
    return await message_models.Message.objects.create(**message.dict(skip_defaults=True))
