from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model


class Message(Model):
    id = fields.IntField(pk=True)
    subject = fields.TextField(null=False)
    message = fields.TextField(null=False)

    class Meta:
        table = 'message'


class MessageSchema(BaseModel):
    id: int = None
    subject: str
    message: str

    class Config:
        orm_mode: True
