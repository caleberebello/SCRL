import flask, requests
from flask import render_template, request
import sys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/<lat1>/<lng1>', methods=['GET'])
def api_prova(lat1, lng1):
    url = f"https://api.sunrise-sunset.org/json?lat=" + lat1 + "&lng=" + lng1
    print(url)
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
    return data

app.run()