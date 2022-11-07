from sys import argv
from os import getenv
from dotenv import load_dotenv
from libs import dialogHandler as dh

from Data import items

from libs import dbManager as dbm
from libs import  pyresponder as pyr


load_dotenv()
PORT = int(getenv("PORT"))


def start_db():
    db = dbm.createDatabase()   # Crear la base de datos
    ## <Tablas>
    #   Usuarios
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "title TEXT NOT NULL", "name TEXT NOT NULL", "lnacimiento INTEGER NOT NULL", "edad INTEGER NOT NULL", "raza INTEGER NOT NULL", "padre INTEGER NOT NULL", "madre INTEGER NOT NULL", "sexo INTEGER NOT NULL", "renombre INTEGER NOT NULL", "nivel INTEGER NOT NULL", "vida REAL NOT NULL", "mana REAL NOT NULL", "mvida INTEGER NOT NULL", "mmana INTEGER NOT NULL", "xp REAL NOT NULL", "heridas INTEGER NOT NULL", "bwin INTEGER NOT NULL", "blose INTEGER NOT NULL", "batallas INTEGER NOT NULL", "tierras INTEGER NOT NULL", "clan INTEGER NOT NULL", "home INTEGER NOT NULL", "live INTEGER NOT NULL",t_name="Usuarios")
    #   Clanes
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", "miembros INTEGER NOT NULL", t_name="Clanes")
    #   Clases
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", t_name="Clases")
    #   Razas
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", t_name="Razas")
    #   Estructuras
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", "action INTEGER NOT NULL", t_name="Estructuras")
    #   Acciones
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", "action INTEGER NOT NULL", "args TEXT NOT NULL", t_name="Acciones")
    #   Items
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", "desc TEXT NOT NULL", "action INTEGER NOT NULL", "FOREIGN KEY(action) REFERENCES Acciones(id)",t_name="Items")
    #   Lugares
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "name TEXT NOT NULL", "dueño INTEGER NOT NULL",  "casas INTEGER NOT NULL", "jugadores INTEGER NOT NULL", "special INTEGER NOT NULL", t_name="Lugares")
    #   Inventory
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY", "items TEXT NOT NULL", "money INTEGER NOT NULL", "cabeza INTEGER NOT NULL", "pecho INTEGER NOT NULL", "muñecas INTEGER NOT NULL", "piernas INTEGER NOT NULL", "zapatos INTEGER NOT NULL", "mano_izq INTEGER NOT NULL", "mano_der INTEGER NOT NULL", "cuello INTEGER NOT NULL", "flechas INTEGER NOT NULL", t_name="Inventory")
    #   Players
    dbm.createTable(db, "id INTEGER NOT NULL PRIMARY KEY", "tusern TEXT NOT NULL", "password TEXT NOT NULL", t_name="Players")
    ## </Tablas>
    return db


def c_start(data:pyr.info):
    resp = "start"
    file = "start"
    if data.HEAD == "/todus":
        ext = "tds"
    elif data.HEAD == "/whatsapp":
        ext = "wht"
    else:
        ext = "raw"
    info = []
    info.append(data.USER)
    resp = dh.generateDialog(f"./Dialogs/{file}.{ext}", *info)
    pyr.addResponse(resp)


def createItems(db):
    Excaliburn = items.createItem(db, name="Excaliburn", desc="Espada sin filo")


def start(*argv):
    db = start_db()
    # put more code here
    pyr.addTrigguer("start", c_start)
    createItems(db) # Crea los items en la base de datos
    strartAt = ("0.0.0.0", PORT)
    # pyr.server_start(strartAt)
    db.close()


if __name__ == "__main__":
    start(*argv)
