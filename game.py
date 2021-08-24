from tinydb import TinyDB, Query
import openpyxl
gamedb = TinyDB('game.json')
user = Query()


def get_cell_value_list(sheet):
    return([[cell.value for cell in row] for row in sheet])

def read_map(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet1']

    all_cell_value = get_cell_value_list(sheet['A1:F6'])
    return all_cell_value


def addMap(userna, readmap):
    exist = gamedb.search(user.username == userna)
    if not exist :
        gamedb.insert({"username": userna, "map": readmap})
    else:
        gamedb.update({'map' : readmap}, user.username == userna)

def attack(name,x,y):
    check = gamedb.search(user.username == name)
    newmap = check[0]['map']
    if check[0]['map'][x][y] == 'x':
        newmap[x][y]= None
        gamedb.update({'map': newmap}, user.username==name)
        return True
    else :
        return False

def checkWin(name):
    check = gamedb.search(user.username == name)
    value = sum(row.count('x') for row in check[0]['map'])
    if value ==0:
        return True;
    else:
        return False;


