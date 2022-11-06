from libs import dbManager as dbm
from Data import users
import hashlib



def generateBorn(db, idPadre, idMadre):
    key = ""
    padre = users.getUserByID(idPadre)[0]
    madre = users.getUserByID(idMadre)[0]
    nPadre = padre[2]
    nMadre = madre[2]
    dPadre = sha256(f"{nPadre}:{idPadre}")
    dMadre = sha256(f"{nMadre}:{idMadre}")
    key = md5(f"[{dPadre}]:[{dMadre}]")
    return key


def sha256(txt:str):
    txt = txt.encode('utf-8')
    txt = hashlib.sha256(txt).hexvalue()
    return txt


def md5(txt:str):
    txt = txt.encode('utf-8')
    txt = hashlib.md5(txt).hexvalue()
    return txt