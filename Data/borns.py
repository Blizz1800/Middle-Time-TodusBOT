import hashlib
from random import randrange

from Data import users
from libs import dbManager as dbm

TABLE = "Borns"
CAMPS = "padre, madre, key, childs"


def generateBorn(db, idPadre, idMadre, childs=0):
    key = ""
    padre = users.getUserByID(db, idPadre)[0]
    madre = users.getUserByID(db, idMadre)[0]
    nPadre = padre[2]
    nMadre = madre[2]
    dPadre = sha256(f"{nPadre}:{idPadre}")
    dMadre = sha256(f"{nMadre}:{idMadre}")
    key = md5(f"[{dPadre}]:[{dMadre}]")
    key = md5(sha256(md5(f"{key}//{randrange(1, 1000000)}")))
    if childs != 0:
        dbm.insertData(db, TABLE, CAMPS, idPadre, idMadre, key, childs)
    prob = randrange(0, 100)
    if prob <= 80:
        childs = 1
    elif prob <= 98:
        childs = 2
    else:
        childs = 3
    dbm.insertData(db, TABLE, CAMPS, idPadre, idMadre, key, childs)
    return


def getKeys(db, id: int):
    return dbm.getData(db, TABLE, CAMPS, f"`padre`={id} OR `madre`={id}")


def clearKeys(db):
    dbm.deleteData(db, TABLE, "`childs`=0")


def sha256(txt: str):
    txt = txt.encode('utf-8')
    txt = hashlib.sha256(txt).hexdigest()
    return txt


def md5(txt: str):
    txt = txt.encode('utf-8')
    txt = hashlib.md5(txt).hexdigest()
    return txt
