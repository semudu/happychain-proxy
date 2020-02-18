import config
import requests
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    response = requests.get(config.API_URL)
    return response.text, response.status_code


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)