from os import getenv
from sys import argv

from dotenv import load_dotenv

from Data import actions
from Data import borns
from Data import items
from Data import users
from libs import dbManager as dbm
from libs import dialogHandler as dh
from libs import pyresponder as pyr

load_dotenv()
PORT = int(getenv("PORT"))

TODUS_P = getenv("TODUS_P")
WHATSAPP_P = getenv("WHATS_P")


def start_db():
    db = dbm.createDatabase()  # Crear la base de datos
    ## <Tablas>
    #   Usuarios
    TUsuarios = dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True),
                                dbm.createCamp("title", dbm.TXT),
                                dbm.createCamp("name", dbm.TXT), dbm.createCamp("lnacimiento", dbm.INT),
                                dbm.createCamp("edad", dbm.INT), dbm.createCamp("raza", dbm.INT),
                                dbm.createCamp("padre", dbm.INT),
                                dbm.createCamp("madre", dbm.INT), dbm.createCamp("sexo", dbm.INT),
                                dbm.createCamp("renombre", dbm.INT), dbm.createCamp("nivel", dbm.INT),
                                dbm.createCamp("vida", dbm.FLOAT), dbm.createCamp("mana", dbm.FLOAT),
                                dbm.createCamp("mvida", dbm.INT), dbm.createCamp("mmana", dbm.INT),
                                dbm.createCamp("xp", dbm.FLOAT),
                                dbm.createCamp("heridas", dbm.INT), dbm.createCamp("bwin", dbm.INT),
                                dbm.createCamp("blose", dbm.INT), dbm.createCamp("batallas", dbm.INT),
                                dbm.createCamp("tierras", dbm.INT), dbm.createCamp("clan", dbm.INT),
                                dbm.createCamp("home", dbm.INT), dbm.createCamp("live", dbm.INT), t_name="Usuarios")
    #   Clanes
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    dbm.createCamp("miembros", dbm.INT), t_name="Clanes")
    #   Clases
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    t_name="Clases")
    #   Razas
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    t_name="Razas")
    #   Estructuras
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    dbm.createCamp("action", dbm.INT), t_name="Estructuras")
    #   Acciones
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    dbm.createCamp("action", dbm.INT), dbm.createCamp("args", dbm.TXT), t_name="Acciones")
    #   Items
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    dbm.createCamp("desc", dbm.TXT), dbm.createCamp("action", dbm.INT),
                    "FOREIGN KEY(action) REFERENCES Acciones(id)", t_name="Items")
    #   Lugares
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True), dbm.createCamp("name", dbm.TXT),
                    dbm.createCamp("dueño", dbm.INT), dbm.createCamp("casas", dbm.INT),
                    dbm.createCamp("jugadores", dbm.INT), dbm.createCamp("special", dbm.INT), t_name="Lugares")
    #   Inventory
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True), dbm.createCamp("items", dbm.TXT),
                    dbm.createCamp("money", dbm.INT), dbm.createCamp("cabeza", dbm.INT),
                    dbm.createCamp("pecho", dbm.INT), dbm.createCamp("muñecas", dbm.INT),
                    dbm.createCamp("piernas", dbm.INT), dbm.createCamp("zapatos", dbm.INT),
                    dbm.createCamp("mano_izq", dbm.INT), dbm.createCamp("mano_der", dbm.INT),
                    dbm.createCamp("cuello", dbm.INT), dbm.createCamp("flechas", dbm.INT), t_name="Inventory")
    #   Players
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True),
                    dbm.createCamp("tusern", dbm.TXT), dbm.createCamp("password", dbm.TXT),
                    dbm.makeForeign("id", TUsuarios, "id", onDelete=dbm.CASCADE, onUpdate=dbm.CASCADE),
                    t_name="Players")
    #   Borns
    dbm.createTable(db, dbm.createCamp("id", dbm.INT, primary=True, ai=True),
                    dbm.createCamp("padre", dbm.INT, default=0), dbm.createCamp("madre", dbm.INT, default=0),
                    dbm.createCamp("key", dbm.TXT), dbm.createCamp("childs", dbm.INT),
                    dbm.makeForeign("padre", "Usuarios", "id", onDelete=dbm.SET_DEF, onUpdate=dbm.CASCADE),
                    dbm.makeForeign("padre", "Usuarios", "id", onDelete=dbm.SET_DEF, onUpdate=dbm.CASCADE),
                    t_name="Borns")
    ## </Tablas>
    return db


def ext(app: str):
    if app == TODUS_P:
        extn = "tds"
    elif app == WHATSAPP_P:
        extn = "wht"
    else:
        extn = "raw"
    return extn


def createResp(file, appPackage, *formatData):
    return dh.generateDialog(f"./Dialogs/{file}.{ext(appPackage)}", *formatData)


def c_start(data: pyr.info):
    resp = createResp("start", data.APP, data.USER)
    pyr.addResponse(resp)


def c_born(data: pyr.info, db):
    msg = data.MESSAGE.split(' ')
    if len(msg) != 2:
        pyr.addResponse(createResp("born_fail", data.APP))
        return
    born = borns.findBorn(db, msg[1])
    if born is not None:
        pyr.addResponse(createResp("born_success", data.APP))
        borns.reduceByOne(db, born[0])
        borns.clearKeys(db)

def c_global(data: pyr.info, db):
    if data.HEAD == "/u_name":
        pass    # Define el Username del player
    else:
        pyr.addResponse(f"No se esperaba: {data.MESSAGE}")

def createItems(db):
    Excaliburn = items.createItem(db, name="Excaliburn", desc="Espada sin filo")


def defaultData(db):
    u_user = users.createDUser(db, "Desconocido", 0)  # Unknown user
    no_action = actions.createAction(db, "NO ACTION", 0)  # No action
    borns.generateBorn(db, 1, 1)


def start(*argv):
    db = start_db()
    borns.clearKeys(db)
    # put more code here
    pyr.addTrigguer("start", c_start)
    pyr.addTrigguer("born", c_born, db)
    pyr.addTrigguer("*", c_global, db)
    createItems(db)  # Crea los items en la base de datos
    itemList = items.loadItems(db) # Carga los items en una lista
    defaultData(db)  # Crea las entradas default de la BD
    strartAt = ("0.0.0.0", PORT)  # Direccion de alojamiento del socket
    pyr.server_start(strartAt) # Inicia el servidor
    db.close()  # Cierra la DB
    # Despues de q el server se detiene


if __name__ == "__main__":
    start(*argv)
