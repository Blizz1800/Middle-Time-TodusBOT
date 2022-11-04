from libs import dbManager as dbm

TABLA = "Items"
CAMPS = "name, desc, action"

def createItem(db, name:str, desc:str, action:int):
    dbm.insertData(db, TABLA, CAMPS, name, desc, action)


def getItems(db):
    return dbm.getData(db, TABLA)


def getItemByID(db, id:int):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=1)


def getItemByName(db, name:str):
    return dbm.getData(db, TABLA, extra=f"`name`='{name}'", many=1)
