from tortoise import fields
from tortoise.models import Model


class Message(Model):
    id = fields.BigIntField(pk=True)
    subject = fields.TextField(null=False)
    message = fields.TextField(null=False)

    class Meta:
        table = 'message'
