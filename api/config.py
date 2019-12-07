from datetime import datetime
from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    # API config
    api_version_header: str = "api-version"
    api_default_version: str = datetime.now().strftime("%Y-%m-%d")
    testing: bool = False

    # Database
    database_url: PostgresDsn
