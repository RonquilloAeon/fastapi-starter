import os

__all__ = ['config']


class Config:
    DB_MODEL_MODULES = ['models']
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_PASS = os.getenv('DB_PASS')
    DB_USER = os.getenv('DB_USER')


config = Config()
