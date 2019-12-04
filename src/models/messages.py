import orm
from pydantic import BaseModel

from db import get_db

db = get_db()


class Message(orm.Model):
    __tablename__ = "message"
    __database__ = db.database
    __metadata__ = db.metadata

    id = orm.Integer(primary_key=True)
    subject = orm.Text(allow_null=False)
    message = orm.Text(allow_null=False)


class MessageSchema(BaseModel):
    id: int = None
    subject: str
    message: str

    class Config:
        orm_mode: True
