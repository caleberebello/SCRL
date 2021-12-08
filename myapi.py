import flask, requests
from flask import render_template, request, redirect, url_for
import sys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        lat1 = request.form["lat1"]
        lng1 = request.form["lng1"]
        return redirect(url_for('api_prova', lat1=lat1, lng1=lng1))
    return render_template('index.html')

@app.route('/<lat1>/<lng1>', methods=['GET'])
def api_prova(lat1, lng1):
    url = f"https://api.sunrise-sunset.org/json?lat=" + lat1 + "&lng=" + lng1
    print(url)
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
    return data

app.run()