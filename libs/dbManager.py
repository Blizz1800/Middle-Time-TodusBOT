import sqlite3

tables = []

INT = "INTEGER"
TXT = "TEXT"
FLOAT = "REAL"

CASCADE = "CASCADE"
NO_ACTION = "NO ACTION"
RESTRICT = "RESTRICT"
SET_NULL = "SET NULL"
SET_DEF = "SET DEFAULT"


def createCamp(camp, type, default="", null=False, primary=False, ai=False):
    if default != "":
        default = f"DEFAULT {default}"
    if primary:
        primary = "PRIMARY KEY"
    else:
        primary = ""
    if ai:
        ai = "AUTOINCREMENT"
    else:
        ai = ""
    if not null:
        null = "NOT NULL"
    else:
        null = ""
    value = f"{camp} {type} {null} {default} {primary} {ai}"
    return value


def makeForeign(camp, refTable, ref, onDelete="", onUpdate=""):
    if onDelete != "":
        onDelete = f"ON DELETE {onDelete}"
    if onUpdate != "":
        onUpdate = f"ON UPDATE {onUpdate}"
    value = f"FOREIGN KEY({camp}) REFERENCES {refTable}({ref}) {onDelete} {onUpdate}"
    return value


def createDatabase(name="database.db"):
    '''
    Crea una base de datos en el directorio actual o se conecta a ella.
    :param name: (Opcional) Nombre de la base de datos.
    :return: Devuelve una conexion a la base de datos creada.
    '''
    try:
        db = sqlite3.connect(f"./{name}")
        cur = db.cursor()
        return db
    except:
        return 0


def createTable(db, *camps, t_name="table"):
    '''
    Crea una tabla nueva si no existe.
    :param db: La base de datos a la q se le hara la consulta.
    :param camps: Los campos de la tabla (ID, Nombre, etc...).
    :param t_name: Nombre de la tabla a crear, por default "table".
    :return: `True` si todo salio bien y `False` si no.
    '''
    try:
        cur = db.cursor()
        if len(camps) == 0:
            return False
        cmps = ""
        rows = ""
        times = 0
        for i in camps:
            cmps += f"{i}"
            # if not "AUTOINCREMENT" in i:
            # rows += f"{i.split(' ')[0]}"
            if times != len(camps) - 1:
                cmps += ", "
                times += 1
                # if not "AUTOINCREMENT" in i:
                # rows += ", "
        query = f"CREATE TABLE IF NOT EXISTS {t_name}({cmps});"
        cur.execute(query)
        db.commit()
        tables.append({"t_name": t_name, "camps": rows})
        cur.close()
        return t_name
    except Exception as e:
        print(e)
        return False


def insertData(db, table, rows, *data):
    '''
    Inserta datos especificos en la base de datos
    :param db: Base de datos a en la q ingresar los datos
    :param table: Tabla en la q ingresar los datos
    :param rows: Campos de la tabla
    :param data: Datos a ingresar **DEBE COINCIDIR LA CANTIDAD DE DATOS CON LA CANTIDAD DE COLUMNAS**
    :return: `True` si no da error, `False` si hay errores
    '''
    cur = db.cursor()
    tmp = ""
    tmp2 = ""
    rows = rows.split(", ")
    if (len(rows) != len(data)):
        print(f"\x1b[1;31mError de longitud de datos para tabla {table}")
        return False
    for i in rows:
        tmp += f"`{i}`"
        if i != rows[len(rows) - 1]:
            tmp += ", "
    times = 0
    for i in data:
        if type(i) is int or type(i) is float:
            tmp2 += f"{i}"
        else:
            tmp2 += f"'{i}'"
        if times != len(data) - 1:
            tmp2 += ", "
            times += 1

    query = f"INSERT INTO {table} ({tmp}) VALUES ({tmp2});"
    cur.execute(query)
    db.commit()
    cur.close()
    return True


def getData(db, tabla, row="*", extra: str = None, many=0):
    if extra is None:
        where = ""
    else:
        where = f"WHERE {extra}"
    query = f"SELECT {row} FROM {tabla} {where}"
    cur: sqlite3.Cursor = db.cursor()
    cur.execute(query)
    content = cur.fetchall()
    cur.close()
    if len(content) > 0:
        if many != 0:
            data = []
            for i in range(0, many):
                data.append(content[i])
            return data
        if len(content) == 1:
            return content[0]
        elif len(content) == 0:
            return None
    return content


def updateData(db, tabla, condition, row, value):
    cur = db.cursor()
    tp = "'"
    if type(value) is int:
        tp = ""
    query = f"UPDATE {tabla} SET `{row}`={tp}{value}{tp} WHERE {condition}"
    cur.execute(query)
    cur.close()
    return True


def dropData(db, tabla, condition):
    cur = db.cursor()
    query = f"DELETE FROM {tabla} WHERE {condition}"
    cur.execute(query)
    cur.close()