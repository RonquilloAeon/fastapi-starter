from fastapi import APIRouter
from typing import List

from api.application.versioning import version, VersionedRoute
from api.application.message import models as message_models

router = APIRouter(route_class=VersionedRoute)


@router.get("", response_model=List[message_models.MessageSchema])
@version("2019", "12", "07")
async def read_messages():
    return await message_models.Message.objects.all()


@router.post("", response_model=message_models.MessageSchema, status_code=201)
@version("2019", "12", "07")
async def write_message(message: message_models.MessageInSchema):
    return await message_models.Message.objects.create(**message.dict())
