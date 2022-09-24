#!/usr/bin/python
#-*- coding: utf-8 -*-
import pymongo
from datetime import datetime, timedelta

# DB 연결
client = pymongo.MongoClient("mongodb+srv://dbUser:1234@cluster0.3fk5bkx.mongodb.net/?retryWrites=true&w=majority")
db = client.deagu_bus
col_info = db.reserveBus_info # 예약 버스 정보
col_state = db.bus_state      # 현재 버스 상태
max_seat = 26
avail_init = (1 << max_seat) - 1

def delete_pre_reserve():
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    col_state.delete_many({'year':yesterday.year, 'month':yesterday.month, 'day':yesterday.day})
    for i in range(1, 18):
        col_state.delete_many({'hour':i})

def insert_next_reserve():
    tomorrow = datetime.now() + timedelta(days=1)
    bus_route_list = col_info.find({'type':'route'})

    search = col_state.find({'year':tomorrow.year, 'month':tomorrow.month, 'day':tomorrow.day})
    for i in search:
        # print("Already insert")
        return
    
    for r in bus_route_list:
        pre_BS = None
        i = 0
        while i != len(r['BS_list'][i]) - 1:
            bus_route = col_info.find({'type':'bus', 'route':r['route'], 'forward':r['forward'], 'BS_name':r['BS_list'][i]})
            for b in bus_route:
                element = {'route':r['route'], 'forward':b['forward'], 'bus_id':b['bus_id'],
                    'BS_on':pre_BS, 'BS_off':r['BS_list'][i],
                    'max_num':max_seat, 'available':avail_init,
                    'year':tomorrow.year, 'month':tomorrow.month, 'day':tomorrow.day,
                    'hour':b['arrive_time']['hour'], 'min':b['arrive_time']['min']}
                print(element)
                col_state.insert_one(element)

            pre_BS = r['BS_list'][i]
            i += 1
    # print(bin(avail_init))

# if __name__ == "__main__":
#     # col_state.delete_many({})
#     delete_pre_reserve()
#     insert_next_reserve()