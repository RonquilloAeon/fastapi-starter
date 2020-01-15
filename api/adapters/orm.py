import databases
from sqlalchemy import (
    Table, MetaData, Column, Integer, Text
)

from api.config import Config

config = Config()
database = databases.Database(config.DATABASE_URL, force_rollback=config.TESTING)
metadata = MetaData()


async def session_factory():
    return database.transaction()


category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
)
