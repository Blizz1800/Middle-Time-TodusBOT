from libs import dbManager as dbm

TABLA = "Items"
CAMPS = "name, desc, action"


def createItem(db, name: str, desc: str, action: int = 0):
    if len(getItemByName(db, name)) != 0:  # Si el item ya existe, devuelve su ID
        return getItemByName(db, name)[0][0]
    # Sino lo crea y añade a la base de datos devolviendo su ID
    dbm.insertData(db, TABLA, CAMPS, name, desc, action)
    return getItemByName(db, name)[0][0]


def getItems(db):
    return dbm.getData(db, TABLA)


def getItemByID(db, id: int, many=1):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=many)


def getItemByName(db, name: str, many=1):
    return dbm.getData(db, TABLA, extra=f"`name`='{name}'", many=many)
