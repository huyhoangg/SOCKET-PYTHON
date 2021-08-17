from tinydb import TinyDB, Query

db = TinyDB('db.json')
user = Query()

def check_user_existed(userInfo):
    result = db.search(user.username == userInfo)
    if result:
        return True
    else :
        return False

def insert_data(name, psw):
    db.insert({'username': name, 'password': psw, 'fullname': '', 'dob': '',
               'note': '', 'point': 0})

def check_pass(name, psw):
    account = db.search(user.username == name)
    password = account[0]['password']
    if password == psw:
        return True
    return False

def update_info(type, name, info):
    if type == 'fullname':
        db.update({'fullname': info}, user.username == name)
    elif type == 'dob':
        db.update({'dob': info}, user.username == name)
    elif type == 'note':
        db.update({'note': info}, user.username == name)
    elif type == 'password':
        db.update({'password': info}, user.username == name)

def check_user_info(type, name):
    result = db.search(user.username == name)

    fname = f"fullname of {name} :{result[0]['fullname']}"
    day = f"dob of {name} : {result[0]['dob']}"
    note = f"note of {name} : {result[0]['note']}"
    point = f"win point of {name} : {result[0]['point']}"
    alldata = f"{fname} \n {day} \n {note} \n {point}"

    if type == '-show_fullname':
        return fname
    elif type == '-show_date':
        return day
    elif type == '-show_note':
        return note
    elif type == '-show_point':
        return point
    elif type == '-show_all':
        return alldata

def add_win(name):
    result = db.search(user.username == name)
    win = result[0]['point'] + 1
    db.update({'point': win }, user.username == name)
