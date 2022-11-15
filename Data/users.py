from libs import dbManager as dbm

TPlayers = "Players"
TABLA = "Usuarios"
CAMPS = "title, name, lnacimiento, edad, raza, padre, madre, sexo, renombre, nivel, vida, mana, mvida, mmana, xp, heridas, bwin, blose, batallas, tierras, clan, home, live"


def createDUser(db, name, sexo):
    if len(getUserByName(db, name)) > 0:
        return getUserByName(db, name)
    title = ""
    madre = 0
    padre = 0
    edad = 0
    raza = 0
    renombre = 0
    nivel = 1
    mvida = 100
    mmana = 1000
    lnacimiento = 0
    vida = float(mvida)
    mana = float(mmana)
    xp = float(0)
    heridas = 0
    bwin = 0
    blose = 0
    batallas = 0
    tierras = 0
    clan = 0
    home = lnacimiento
    live = 1
    data = (
        title, name, lnacimiento, edad, raza, padre, madre, sexo, renombre, nivel, vida, mana, mvida, mmana, xp,
        heridas,
        bwin, blose, batallas, tierras, clan, home, live)
    dbm.insertData(db, TABLA, CAMPS, *data)
    return getUserByName(db, name)


def createUser(db, name, lnacimiento, padre, madre, sexo, mvida, mmana):
    if len(getUserByName(db, name)) > 0:
        return getUserByName(db, name)
    title = ""
    edad = 0
    raza = getUserByID(db, madre)[4]
    renombre = 0
    nivel = 1
    vida = float(mvida)
    mana = float(mmana)
    xp = float(0)
    heridas = 0
    bwin = 0
    blose = 0
    batallas = 0
    tierras = 0
    clan = getUserByID(db, padre)[21]
    home = lnacimiento
    data = (
        title, name, lnacimiento, edad, raza, padre, madre, sexo, renombre, nivel, vida, mana, mvida, mmana, xp,
        heridas,
        bwin, blose, batallas, tierras, clan, home)
    dbm.insertData(db, TABLA, CAMPS, *data)
    return getUserByName(db, name)


def getUsers(db):
    return dbm.getData(db, TABLA)


def getUserByID(db, id: int):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=1)


def getUserByName(db, name: str, many=1):
    return dbm.getData(db, TABLA, extra=f"`name`='{name}'", many=many)


def getTUserByID(db, id: int, many=1):
    return dbm.getData(db, TPlayers, extra=f"`id`={id}", many=many)


def getTUserByName(db, name: str, many=1):
    return dbm.getData(db, TPlayers, extra=f"`tusern`='{name}'", many=many)


def getUsersByMID(db, id: int, many=0):
    return dbm.getData(db, TABLA, extra=f"`madre`={id}", many=many)


def getUsersByFID(db, id: int, many=0):
    return dbm.getData(db, TABLA, extra=f"`padre`={id}", many=many)


def getDecendants(db, id: int, many=0):
    users = getUsers(db)
    descendants = []
    self = getUserByID(db, id)[8]
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
