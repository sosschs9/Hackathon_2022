#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo
from datetime import datetime

# DB 연결
client = pymongo.MongoClient("mongodb+srv://dbUser:1234@cluster0.3fk5bkx.mongodb.net/?retryWrites=true&w=majority")
db = client.deagu_bus
col_info = db.reserveBus_info  # 예약버스 정보
col_bus = db.bus_state  # 현재 버스 상태
col_reserve = db.reservation  # 예약 내역


# 모든 예약버스 노선의 정류장 반환
def return_all_route_list():
    res = []
    search = col_info.find({'type': 'route'})
    for i in search:
        res.append({'route': i['route'], 'forward': i['forward'], 'BS_list': i['BS_list']})

    return res


# 유효한 시간인지 확인
def check_date(element):
    today = datetime.now()
    if (element["year"] < today.year):
        return False
    if (element['year'] > today.year):
        return True
    if (element['month'] < today.month):
        return False
    if (element['month'] > today.month):
        return True
    if (element['day'] < today.day):
        return False
    if (element['day'] > today.day):
        return True
    if (element['hour'] < today.hour):
        return False
    if (element['hour'] > today.hour):
        return True
    if (element['min'] < int(today.strftime('%M'))):
        return False
    return True


# 예약내역 불러오기
def return_reservation(user_id, user_pw):
    search = col_reserve.find({'user_id': user_id, 'user_pw': user_pw})
    for i in search:
        if (~check_date(i)):
            i['reserve_vaild'] = False


# 도착까지 남은 시간(1시간 이내), 도착 정보 반환
def return_remain_time(element):
    today = datetime.now()
    # print(element)
    str_time = str(element['hour']) + ":" + str(element['min']) + " 도착"
    if (element['year'] != today.year):
        return str_time
    if (element['month'] != today.month):
        return str_time
    if (element['day'] != today.day):
        return str_time
    gap = element['hour'] * 60 + element['min'] - (int(today.strftime('%H')) * 60 + int(today.strftime('%M')))
    if (gap < 60):
        return str(gap) + "분(" + str_time + ")"
    else:
        return str_time


# 예약내역 불러오기
def return_reservation(user_id, user_pw):
    search = col_reserve.find({'user_id': user_id, 'user_pw': user_pw})
    result = []
    for i in search:
        if (~check_date(i)):
            i['reserve_vaild'] = False
            col_reserve.delete_one({'_id': i['_id']})
            col_reserve.insert_one(i)
        if (i['reserve_vaild']):
            result.append(i)
    return result


# 예약 취소
def cancle_reserve(reserve_id):
    res = col_reserve.find_one({'_id': reserve_id})
    res['reserve_vaild'] = False
    # print(res)
    col_reserve.delete_one({'_id': reserve_id})
    col_reserve.insert_one(res)

    BS_find = res['BS_on']
    seat_num = 1 << (res['seat'] - 1)

    while True:
        search = col_bus.find_one({"bus_id": res['bus_id'], "BS_on": BS_find})
        search["available"] = search["available"] | seat_num
        # print(search)
        # print(bin(search['available']))

        col_bus.delete_one({"bus_id": res['bus_id'], "BS_on": BS_find})
        col_bus.insert_one(search)

        if search["BS_off"] == res["BS_off"]:
            break
        BS_find = search["BS_off"]


# 예약하기
def reserve_seat(user_id, user_pw, bus_id, BS_on, BS_off, seat):
    BS_find = BS_on
    seat_num = ~(1 << (seat - 1))
    start = col_bus.find_one({"bus_id": bus_id, "BS_on": BS_find})
    element = {'reserve_valid': True, 'user_id': user_id, 'user_pw': user_pw, 'route': start['route'], 'bus_id': bus_id,
               'BS_on': BS_on, 'BS_off': BS_off, 'seat': seat,
               'year': start['year'], 'month': start['month'], 'day': start['day'],
               'hour': start['hour'], 'min': start['min']}
    col_reserve.insert_one(element)

    while True:
        search = col_bus.find_one({"bus_id": bus_id, "BS_on": BS_find})
        search["available"] = search["available"] & seat_num

        # print(bin(search['available']))

        col_bus.delete_one({"bus_id": bus_id, "BS_on": BS_find})
        col_bus.insert_one(search)

        if search["BS_off"] == BS_off:
            break
        BS_find = search["BS_off"]


# 해당 버스에서 예약가능한 좌석 알아내기
def count_avail(bus_id, BS_on, BS_off, max):
    BS_find = BS_on
    avail = (1 << max) - 1
    while True:
        search = col_bus.find_one({"bus_id": bus_id, "BS_on": BS_find})
        and_res = avail & search["available"]
        avail = and_res

        if search["BS_off"] == BS_off:
            break
        BS_find = search["BS_off"]

    count = 0
    temp = avail
    while temp:
        if temp & 1:
            count += 1
        temp = temp >> 1

    return avail, count

#bus_id와 출발/도착 정류장 -> 좌석 현황 리스트
def return_seat_status(bus_id, BS_on, BS_off):
    avail_result, count_result = count_avail(bus_id, BS_on, BS_off, 26)
    avail_list = []
    for j in range(0, 26):
        if(avail_result & (1 << j)):
            avail_list.append(True)
        else :
            avail_list.append(False)

    return avail_list


# 버스노선, 방향, 타는/내리는 정류장 -> 버스 목록 찾기
def search_bus(route, forward, BS_on, BS_off):
    result = []
    search = col_bus.find({"route": route, "BS_on": BS_on, "forward": forward})
    for i in search:
        if check_date(i):
            # print(i)
            avail_result, count_result = count_avail(i["bus_id"], BS_on, BS_off, i['max_num'])
            avail_list = []
            for j in range(0, i["max_num"]):
                if(avail_result & (1 << j)):
                    avail_list.append(True)
                else :
                    avail_list.append(False)
            result.append({"route": i["route"], "bus_id": i["bus_id"], "max_num": i["max_num"], "available": count_result,
                 "seat_state": avail_list, 'time': return_remain_time(i)})

    return result