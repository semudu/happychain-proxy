import requests
from flask import Flask
from requests.auth import HTTPBasicAuth

import config

app = Flask(__name__)
auth = HTTPBasicAuth(config.USERNAME, config.PASSWORD)


@app.route("/")
def hello():
    response = requests.get(config.API_URL)
    return response.text, response.status_code


@app.route("/transaction/received/team/<team_id>")
def get_received_transactions(team_id):
    response = requests.get(config.API_URL + "/transaction/received/team/" + team_id, auth=auth)
    return response.json(), response.status_code


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
