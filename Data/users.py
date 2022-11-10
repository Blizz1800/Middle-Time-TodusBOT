from libs import dbManager as dbm

TPlayers = "Players"
TABLA = "Usuarios"
CAMPS = "title, name, lnacimiento, edad, raza, padre, madre, sexo, renombre, nivel, vida, mana, mvida, mmana, xp, heridas, bwin, blose, batallas, tierras, clan, home"


'''
    Falta añadir la funcion para crear users
'''

def getUsers(db):
    return dbm.getData(db, TABLA)

def getUserByID(db, id:int):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=1)


def getUserByName(db, name:str, many=1):
    return dbm.getData(db, TABLA, extra=f"`name`='{name}'", many=many)


def getTUserByID(db, id:int, many=1):
    return dbm.getData(db, TPlayers, extra=f"`id`={id}", many=many)


def getTUserByName(db, name:str, many=1):
    return dbm.getData(db, TPlayers, extra=f"`tusern`='{name}'", many=many)


def getUsersByMID(db, id:int, many=0):
    return dbm.getData(db, TABLA, extra=f"`madre`={id}", many=many)
def getUsersByFID(db, id:int, many=0):
    return dbm.getData(db, TABLA, extra=f"`padre`={id}", many=many)

def getDecendants(db, id:int, many=0):
    users = getUsers(db)
    descendants = []
    self = getUserByID(id)[8]
    if self == 1:
        sex = 6
    else:
        sex = 7
    for user in users:
        if user[sex] == id:
            descendants.append(user)
        else:
            continue
    return descendants
