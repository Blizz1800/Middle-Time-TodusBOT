from libs import dbManager as dbm


TABLA = "Usuarios"
CAMPS = "title, name, lnacimiento, edad, raza, padre, madre, sexo, renombre, nivel, vida, mana, mvida, mmana, xp, heridas, bwin, blose, batallas, tierras, clan, home"


def getUserByID(db, id:int):
    return dbm.getData(db, TABLA, extra=f"`id`={id}", many=1)