from tinydb import TinyDB, Query

db = TinyDB('db.json')
user = Query()

def check_user_existed(userInfo):
    result = db.search(user.username == userInfo)
    if result:
        return False
    else :
        return True

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

def check_user_info(type, name):
    result = db.search(user.username == name)

    fname = result[0]['fullname']
    day = result[0]['dob']
    note = result[0]['note']
    point = result[0]['point']

    if type == 'fullname':
        return fname
    elif type == 'dob':
        return day
    elif type == 'note':
        return note
    elif type == 'point':
        return point

def add_win(name):
    result = db.search(user.username == name)
    win = result[0]['point'] + 1
    db.update({'point': win }, user.username == name)

