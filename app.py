from flask import Flask
from flask_cors import CORS

from config import *

from api.v1.routes import api as api_v1

from utils.logger import logger, default_format

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(api_v1, url_prefix='/v1')

logger.add(sink="log/{time}.log",
           rotation="00:00",
           retention='1 week',
           enqueue=True,
           diagnose=False,
           level="SUCCESS",
           format=default_format,
           encoding='utf-8'
           )

if __name__ == "__main__":
    app.run(**run_config)
