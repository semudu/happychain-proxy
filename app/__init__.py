import config
from .app import app

def run():
    app.run(host=config.HOST, port=config.PORT)