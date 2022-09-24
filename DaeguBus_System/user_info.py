import sys
import pymongo

client = pymongo.MongoClient("mongodb+srv://dbUser:1234@cluster0.3fk5bkx.mongodb.net/?retryWrites=true&w=majority")
db = client.deagu_bus
col_user = db.user_info

def search_user_name(name):
    """
    DB에 name에 해당하는 아이디가 있는지 검색
    """
    search = col_user.find_one({"name": name})
    count = col_user.count_documents({"name": name})

    if(count != 0): return True, search["_id"]
    else: return False, None


def check_user_pw(user_id, password):
    """
    아이디와 패스워드가 일치하는지 확인
    """
    check = col_user.find({"_id":user_id})["password"]
    if (check == password): return True, True
    else: return False, False

def return_user_type(user_id):
    """
    사용자 유형 반환
    """
    type = col_user.find({"_id":user_id})["type"]
    return True, type

def add_user(name, password, type):
    """
    DB 저장
    """
    is_search, user_id = search_user_name(name)
    
    if(is_search == True): return False
    else:
        col_user.insert_one({"name": name, "password": password, "type": type})
        return True


"""
res = add_user("sosschs1", "1234", "NP")

if (res == True):
    search = col_user.find()
    for i in search :
        print(i)
else:
    print("아이디가 중복입니다.")

"""