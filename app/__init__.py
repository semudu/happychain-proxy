import config
from app import app

def run():
    app.run(config.HOST, config.PORT)