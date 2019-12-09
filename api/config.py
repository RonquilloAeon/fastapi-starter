from datetime import datetime
from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    # API config
    API_VERSION_HEADER: str = "api-version"
    API_DEFAULT_VERSION: str = datetime.now().strftime("%Y-%m-%d")
    TESTING: bool = False

    # Database
    DATABASE_URL: PostgresDsn

    class Config:
        case_sensitive = True
