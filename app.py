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
    return render_template('reserve.html', bus_list=bus_list)

# 예약 버스 이름, 출발지, 도착지 입력 -> 예약 버스 리스트 조회 기능
@app.route('/bus_watch', methods=['GET','POST'])
def bus_watch():
    error = None
    if request.method == 'POST':
        route = request.form['bus_name']
        forward = request.form['forward']
        bs_on = request.form['startStation']
        bs_off = request.form['endStation']

        fw = open("cur_info.txt", "w")
        fw.write(bs_on + '\n')
        fw.write(bs_off + '\n')
        fw.write(route + '\n')
        fw.write(forward)

        bus_list = search_bus(route, int(forward), bs_on, bs_off)
        return render_template('bus_watch.html', bus_list=bus_list)


# 버스 정류장 입력 -> 버스 정보 조회 기능
@app.route('/bus_station', methods=['POST'])
def bus_station():
    data = requests.get("http://localhost:8080/station/search/" + request.form['bus_station'])
    return render_template('bus_station.html', data=data)

# 예약 버스 좌석 선택 기능
@app.route('/bus_seat', methods=['GET', 'POST'])
def bus_seat():
    bus_id = request.form['bus_id']

    fp = open("cur_info.txt", "r")
    if request.method == "POST":
        bs_on = fp.readline()
        bs_on = bs_on.strip('\n')
        bs_off = fp.readline().strip('\n')

        fp.close()

        fp = open("cur_info.txt", "a")
        fp.write('\n' + bus_id)

        seat_list = return_seat_status(int(bus_id), bs_on, bs_off)
        return render_template('bus_seat.html', seat_list=seat_list)

# 좌석 선택 확인 -> 중복 값 검사
@app.route('/bus_select_check', methods=['POST'])
def bus_select_check():
    if request.method == 'POST':
        seat = int(request.form['seat_name'])

        fp = open("cur_info.txt", "r")
        bs_on = fp.readline().strip('\n')
        bs_off = fp.readline().strip('\n')
        route = fp.readline().strip('\n')
        forward = int(fp.readline().strip('\n'))
        if (forward == 1):
            str_forward = "정방향"
        else:
            str_forward = "역방향"
        bus_id = int(fp.readline().strip('\n'))

        #arrive_time 도착 정보 추가해야함

        return render_template('bus_select_check.html', bs_on=bs_on, bs_off=bs_off, route=route, forward=str_forward, bus_id=bus_id, seat=seat)

# 회원 아이디, 비밀번호 입력 -> 버스 예약 (버스 번호, 출발지, 도착지, 좌석 등이 담겨 있어야 함. DB저장)
@app.route('/bus_reserve_seat', methods=['POST'])
def bus_reserve_seat():
    if request.method == 'POST':
        user_id = request.form['username']
        print(user_id)
        user_pw = request.form['password']
        print(user_pw)
        bs_on = request.form['bs_on']
        print(bs_on)
        bs_off = request.form['bs_off']
        print(bs_off)
        bus_id = int(request.form['bus_id'])
        print(bus_id)
        seat = int(request.form['seat'])
        print(seat)

        reserve_seat(user_id, user_pw, bus_id, bs_on, bs_off, seat)
        return render_template('view_reservation.html')

# 회원 아이디, 비밀번호 입력 -> 예약 조회
@app.route('/view_reservation', methods=['GET', 'POST'])
def view_reservation():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        reservation_list = return_reservation(user_id, user_pw)
        print(reservation_list)

        correct = return_reservation(user_id, user_pw)
        if(correct == False):
            return render_template('view_reservation.html', correct=False)
        else:
            return render_template('user_reservation.html', user_id=user_id, reservation_list=reservation_list)
    else:
        return render_template('view_reservation.html', correct=True)
#
# @app.route('/delete_reservation', methods=['GET', 'POST'])
# def delete_reservation():


if __name__ == '__main__':
    app.run()
