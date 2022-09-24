import requests
from flask import Flask, render_template, request
import time

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def home():
    return render_template("main.html")

# 버스 예약 페이지
@app.route('/reserve')
def reserve():

    return render_template('reserve.html')

# 예약 버스 이름, 출발지, 도착지 입력 -> 예약 버스 노선 조회 기능
@app.route('/bus_watch', methods=['POST'])
def bus_watch():
    error = None
    if request.method == 'POST':
        busname = request.form['busname']
        return render_template('bus_watch.html', name=busname)

# 버스 정류장 입력 -> 버스 정보 조회 기능
@app.route('/bus_station', methods=['POST'])
def bus_station():
    data = requests.get("http://localhost:8080/station/search/" + request.form['bus_station'])
    return render_template('bus_station.html', data=data)

# 예약 버스 좌석 선택 기능
@app.route('/bus_seat')
def bus_seat():
    return render_template('bus_seat.html')

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
