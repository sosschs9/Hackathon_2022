import requests, json
from flask import Flask, render_template, request
from reserve_bus import *
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/reserve')
def reserve():
    return render_template('reserve.html')

@app.route('/nonreserve')
def nonreserve():
    return render_template('nonreserve.html')

@app.route('/nonreserve_route',methods=['POST'])
def nonreserve_route():
    data = requests.get("http://localhost:8080/route/search/" + request.form['nonreserve_route']).text
    data = json.loads(data)
    buscollect = []
    for var in data:
        routeID = var['버스id']
        busdata = requests.get("http://localhost:8080/route/" + routeID).text
        busdata = json.loads(busdata)
        buscollect.append(busdata)
    size = len(buscollect)
    return render_template('nonreserve_route.html',data=data, buscollect=buscollect,size=size)
     
@app.route('/bus_watch', methods=['POST'])
def bus_watch():
    error = None
    if request.method == 'POST':
        route = request.form['bus_name']
        forward = request.form['forward']
        bs_on = request.form['startStation']
        bs_off = request.form['endStation']
        
        return render_template('bus_watch.html')

@app.route('/nonbus_watch', methods=['POST'])
def nonbus_watch():
    error = None
    if request.method == 'POST':
        bus_name = request.form['bus_name']
        bus_forward = request.form['bus_forward']
        bus_nf = request.form['bus_nf']
        bs_on = request.form['startStation']
        bs_off = request.form['endStation']

        fw = open("cur_info.txt", "w")
        fw.write(bus_name + '\n')
        fw.write(bus_forward + '\n')
        fw.write(bus_nf + '\n')
        fw.write(bs_on + '\n')
        fw.write(bs_off + '\n')
        
        data = requests.get("http://localhost:8080/station/search/" + bs_on).text
        data=json.loads(data)
        stationID = data[0]['정류장id']
        busdata = requests.get("http://localhost:8080/stationrow/" + stationID).text  
        busdata=json.loads(busdata)
        return render_template('nonbus_watch.html', data=data,busdata=busdata,bus_name=bus_name,bus_forward=bus_forward)

@app.route('/nonbus_select_check', methods=['POST'])
def nonbus_select_check():
    if request.method == 'POST':
        bus_id = request.form['bus_id']

        fp = open("cur_info.txt", "r")
        bus_name = fp.readline().strip('\n')
        bus_forward = fp.readline().strip('\n')
        bus_nf = fp.readline().strip('\n')
        bs_on = fp.readline().strip('\n')
        bs_off = fp.readline().strip('\n')

        return render_template('nonbus_select_check.html', bus_name = bus_name, bs_on=bs_on, bs_off=bs_off, bus_id=bus_id)

@app.route('/bus_station', methods=['POST'])
def bus_station():
    data = requests.get("http://localhost:8080/station/search/" + request.form['bus_station']).text
    data=json.loads(data)
    stationID = data[0]['정류장id']
    busdata = requests.get("http://localhost:8080/station/" + stationID).text
    busdata=json.loads(busdata)
    return render_template('bus_station.html', data=data,busdata=busdata)



if __name__ == '__main__':
    app.run()
