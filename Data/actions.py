from libs import dbManager as dbm

TABLA = "Acciones"
CAMPS = "name, action, args"

def createAction(db, name:str, action:int, args:str = None):
    if len(getActionsByName(db, name)) != 0:       # Si ya existe, devuelve su ID
        return getActionsByName(db, name)[0][0]
    # Sino la crea y añade a la base de datos devolviendo su ID
    dbm.insertData(db, TABLA, CAMPS, name, action, args)
    return getActionsByName(db, name)[0][0]


def getActions(db):
    return dbm.getData(db, TABLA)


def getActionsByID(db, id:int, many=1):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=many)


def getActionsByName(db, name:str, many=1):
    return dbm.getData(db, TABLA, extra=f"`name`='{name}'", many=many)
