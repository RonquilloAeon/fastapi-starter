import orm
from pydantic import BaseModel

from api.db import database, metadata


class Message(orm.Model):
    __tablename__ = "message"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    subject = orm.Text(allow_null=False)
    message = orm.Text(allow_null=False)


class MessageInSchema(BaseModel):
    subject: str
    message: str

    class Config:
        orm_mode: True


class MessageSchema(MessageInSchema):
    id: int = None
