import databases
import sqlalchemy
from typing import Optional

from api.config import Config


db = None


class DB:
    def __init__(self, database_url: str, *database_args, **database_kwargs) -> None:
        self.database_url = database_url
        self.database = databases.Database(database_url, *database_args, **database_kwargs)
        self.metadata = sqlalchemy.MetaData()
        # self.engine = sqlalchemy.create_engine(database_url, connect_args={"check_same_thread": False})


def get_db(*database_args, database_url: Optional[str] = None, **database_kwargs) -> DB:
    global db

    if database_url is None:
        database_url = Config().database_url  # Default is db from config.

    if db is None:
        db = DB(database_url, *database_args, **database_kwargs)

    return db
