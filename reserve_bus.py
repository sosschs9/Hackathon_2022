#!/usr/bin/python
#-*- coding: utf-8 -*-
import pymongo
from datetime import datetime

# DB 연결
client = pymongo.MongoClient("mongodb+srv://dbUser:1234@cluster0.3fk5bkx.mongodb.net/?retryWrites=true&w=majority")
db = client.deagu_bus
col_info = db.reserveBus_info       # 예약버스 정보
col_bus = db.bus_state      # 현재 버스 상태
col_reserve = db.reservation    # 예약 내역

def return_all_route_list() :
    res = []
    search = col_info.find({'type':'route'})
    for i in search:
        res.append({'route':i['route'], 'forward':i['forward'], 'BS_list':i['BS_list']})
    
    return res

def check_date(element):
    today = datetime.now()
    if(element["year"] < today.year) :
        return False
    if(element['year'] > today.year) :
        return True
    if(element['month'] < today.month) :
        return False
    if(element['month'] > today.month) :
        return True
    if(element['day'] < today.day) :
        return False
    if(element['day'] > today.day) :
        return True
    if(element['hour'] < today.hour) :
        return False
    if(element['hour'] > today.hour) :
        return True
    if(element['min'] < today.min) :
        return False
    return True

def return_remain_time(element):
    today = datetime.now()
    # print(element)
    str_time = str(element['hour'])+":"+str(element['min'])+" 도착"
    if(element['year'] != today.year) :
        return str_time
    if(element['month'] != today.month) :
        return str_time
    if(element['day'] != today.day) :
        return str_time
    gap = element['hour'] * 60 + element['min'] - (int(today.strftime('%H')) * 60 + int(today.strftime('%M')))
    if(gap < 60):
        return str(gap)+"분("+str_time+")"
    else:
        return str_time


def cancle_reserve(reserve_id):
    res = col_reserve.find_one({'_id':reserve_id})
    res['reserve_vaild'] = False
    # print(res)
    col_reserve.delete_one({'_id':reserve_id})
    col_reserve.insert_one(res)

    BS_find = res['BS_on']
    seat_num = 1<<(res['seat']-1)

    while True:
        search = col_bus.find_one({"bus_id":res['bus_id'], "BS_on":BS_find})
        search["available"] = search["available"] | seat_num
        # print(search)
        # print(bin(search['available']))

        col_bus.delete_one({"bus_id":res['bus_id'], "BS_on":BS_find})
        col_bus.insert_one(search)

        if search["BS_off"] == res["BS_off"] :
            break
        BS_find = search["BS_off"]

def reserve_seat(user_id, user_pw, bus_id, BS_on, BS_off, seat) :
    BS_find = BS_on
    seat_num = ~(1<<(seat-1))
    start = col_bus.find_one({"bus_id":bus_id, "BS_on":BS_find})
    element = {'reserve_valid':True,'user_id':user_id, 'user_pw':user_pw, 'route':start['route'], 'bus_id':bus_id, 'BS_on':BS_on, 'BS_off':BS_off, 'seat':seat,
        'year':start['year'], 'month':start['month'], 'day':start['day'],
        'hour':start['hour'], 'min':start['min']}
    col_reserve.insert_one(element)

    while True:
        search = col_bus.find_one({"bus_id":bus_id, "BS_on":BS_find})
        search["available"] = search["available"] & seat_num

        # print(bin(search['available']))

        col_bus.delete_one({"bus_id":bus_id, "BS_on":BS_find})
        col_bus.insert_one(search)

        if search["BS_off"] == BS_off :
            break
        BS_find = search["BS_off"]

def count_avail(bus_id, BS_on, BS_off, max) :
    BS_find = BS_on
    avail = (1 << max) - 1
    while True:
        search = col_bus.find_one({"bus_id":bus_id, "BS_on":BS_find})
        and_res = avail & search["available"]
        avail = and_res

        if search["BS_off"] == BS_off :
            break
        BS_find = search["BS_off"]

    count = 0
    temp = avail
    while temp :
        if temp & 1 :
            count += 1
        temp = temp >> 1

    return avail, count


def search_bus(route, forward, BS_on, BS_off) :
    result = []
    search = col_bus.find({"route":route, "BS_on":BS_on, "forward":forward})
    for i in search :
        if check_date(i) :
            # print(i)
            avail_result, count_result = count_avail(i["bus_id"], BS_on, BS_off, i['max_num'])
            result.append({"route":i["route"], "bus_id":i["bus_id"], "max_num":i["max_num"], "available":count_result, "seat_state":bin(avail_result), 'time':return_remain_time(i)})

    return result