import requests
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/reserve')
def reserve():

    return render_template('reserve.html')

@app.route('/bus_watch', methods=['POST'])
def bus_watch():
    error = None
    if request.method == 'POST':
        busname = request.form['busname']
        return render_template('bus_watch.html', name=busname)

@app.route('/bus_station', methods=['POST'])
def bus_station():
    data = requests.get("http://localhost:8080/station/search/" + request.form['bus_station'])
    return render_template('bus_station.html', data=data)

@app.route('/bus_seat')
def bus_seat():
    return render_template('bus_seat.html')

if __name__ == '__main__':
    app.run()
