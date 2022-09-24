import requests
from flask import Flask, render_template, request
from reserve_bus import *

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    return render_template("main.html")

# 버스 예약 페이지
@app.route('/reserve')
def reserve():
    bus_list = return_all_route_list()
    print(bus_list)
    return render_template('reserve.html', bus_list=bus_list)

# 예약 버스 이름, 출발지, 도착지 입력 -> 예약 버스 리스트 조회 기능
@app.route('/bus_watch', methods=['POST'])
def bus_watch():
    error = None
    if request.method == 'POST':
        route = request.form['bus_name']
        forward = request.form['forward']
        bs_on = request.form['startStation']
        bs_off = request.form['endStation']

        bus_list = search_bus(route, int(forward), bs_on, bs_off)
        print(bus_list)
        return render_template('bus_watch.html', bus_list=bus_list)

# 버스 정류장 입력 -> 버스 정보 조회 기능
@app.route('/bus_station', methods=['POST'])
def bus_station():
    data = requests.get("http://localhost:8080/station/search/" + request.form['bus_station'])
    return render_template('bus_station.html', data=data)

# 예약 버스 좌석 선택 기능
@app.route('/bus_seat', methods=['POST'])
def bus_seat():
    bus_id = request.form['bus_id']

    seat_list = []

    return render_template('bus_seat.html', seat_list=seat_list)

# 회원 아이디, 비밀번호 입력 -> 버스 예약 (버스 번호, 출발지, 도착지, 좌석 등이 담겨 있어야 함. DB저장)
@app.route('/bus_reserve_seat', methods=['POST'])
def bus_reserve_seat():

    return

# 회원 아이디, 비밀번호 입력 -> 예약 조회
@app.route('/view_reservation', methods=['POST'])
def view_reservation():
    return render_template('view_reservation.html')

if __name__ == '__main__':
    app.run()
