import os
from datetime import datetime

__all__ = ['config']


class Config:
    # API config
    API_VERSION_HEADER_NAME = os.getenv('API_VERSION_HEADER_NAME', 'api-version').lower()
    API_DEFAULT_VERSION = os.getenv('API_DEFAULT_VERSION', datetime.now().strftime('%Y-%m-%d'))

    # Database
    DB_MODEL_MODULES = ['models.messages']
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_PASS = os.getenv('DB_PASS')
    DB_USER = os.getenv('DB_USER')


config = Config()
