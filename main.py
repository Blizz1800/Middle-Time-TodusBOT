from sys import argv

from libs import dbManager as dbm


def start_db():
    db = dbm.createDatabase()
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", "lnacimiento INTEGER NOT NULL", "edad INTEGER NOT NULL", "raza INTEGER NOT NULL", "madre INTEGER NOT NULL", "madre INTEGER NOT NULL", "sexo INTEGER NOT NULL", "renombre INTEGER NOT NULL", "nivel INTEGER NOT NULL", "vida REAL NOT NULL", "mana REAL NOT NULL", "mvida INTEGER NOT NULL", "mmana INTEGER NOT NULL", "xp REAL NOT NULL", "heridas INTEGER NOT NULL", "bwin INTEGER NOT NULL", "blose INTEGER NOT NULL", "batallas INTEGER NOT NULL", "tierras INTEGER NOT NULL", "clan INTEGER NOT NULL", "home INTEGER NOT NULL", t_name="Usuarios")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", "miembros INTEGER NOT NULL", t_name="Clanes")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", t_name="Clases")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", t_name="Razas")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", "action INTEGER NOT NULL", t_name="Estructuras")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", "action INTEGER NOT NULL", "args TEXT NOT NULL", t_name="Acciones")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", "desc TEXT NOT NULL", "action INTEGER NOT NULL", t_name="Items")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "nombre TEXT NOT NULL", "dueño INTEGER NOT NULL",  "casas INTEGER NOT NULL", "jugadores INTEGER NOT NULL", "special INTEGER NOT NULL", t_name="Lugares")
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "items TEXT NOT NULL", "money INTEGER NOT NULL", "cabeza INTEGER NOT NULL", "pecho INTEGER NOT NULL", "muñecas INTEGER NOT NULL", "piernas INTEGER NOT NULL", "zapatos INTEGER NOT NULL", "mano_izq INTEGER NOT NULL", "mano_der INTEGER NOT NULL", "cuello INTEGER NOT NULL", "flechas INTEGER NOT NULL", t_name="Inventory")
    return db


def start(*argv):
    db = start_db()
    # put more code here
    db.close()


if __name__ == "__main__":
    start(*argv)
