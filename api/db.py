import databases
import sqlalchemy

from api.config import Config

config = Config()
database = databases.Database(config.database_url, force_rollback=config.testing)
metadata = sqlalchemy.MetaData()
