from tortoise import Tortoise

__all__ = ['init', 'Tortoise']


async def init(config):
    c = {
        'connections': {
            'default': {
                'engine': 'tortoise.backends.asyncpg',
                'credentials': {
                    'host': config.DB_HOST,
                    'port': config.DB_PORT,
                    'user': config.DB_USER,
                    'password': config.DB_PASS,
                    'database': config.DB_NAME,
                },
            },
        },
        'apps': {
            'models': {
                'models': config.DB_MODEL_MODULES,
            },
        },
    }
    await Tortoise.init(config=c)
