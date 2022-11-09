from libs import dbManager as dbm

TPlayers = "Players"
TABLA = "Usuarios"
CAMPS = "title, name, lnacimiento, edad, raza, padre, madre, sexo, renombre, nivel, vida, mana, mvida, mmana, xp, heridas, bwin, blose, batallas, tierras, clan, home"


def getUserByID(db, id:int, many=1):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=many)


def getUserByName(db, name:str, many=1):
    return dbm.getData(db, TABLA, extra=f"`name`={name}", many=many)


def getTUserByID(db, id:int, many=1):
    return dbm.getData(db, TPlayers, extra=f"`id`={id}", many=many)


def getTUserByName(db, name:str, many=1):
    return dbm.getData(db, TPlayers, extra=f"`tusern`={name}", many=many)