import databases
import sqlalchemy

from api.config import Config

config = Config()
database = databases.Database(config.DATABASE_URL, force_rollback=config.TESTING)
metadata = sqlalchemy.MetaData()
