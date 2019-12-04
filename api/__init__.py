from api.config import Config
from api.main import create_app


app = create_app(Config())
