import sqlite3

tables = []

def createDatabase(name = "database.db") -> tuple:
	try:
		db = sqlite3.connect(f"./{name}")
		cur = db.cursor()
		return (db, cur)
	except:
		return 0
	
def createTable(db, *camps, t_name = "table") -> bool:
        try:
                cur = db.cursor()
                if len(camps) == 0:
                        return False
                cmps = ""
                rows = ""
                for i in camps:
                        cmps += f"{i}"
                        #if not "AUTOINCREMENT" in i:
                                #rows += f"{i.split(' ')[0]}"
                        if i != camps[len(camps)-1]:
                                cmps += ", "
                                #if not "AUTOINCREMENT" in i:
                                        #rows += ", "
                query = f"CREATE TABLE IF NOT EXISTS {t_name}({cmps});"
                cur.execute(query)
                db.commit()
                tables.append({"t_name": t_name, "camps": rows})
                cur.close()
                return True
        except Exception as e:
                print(e)
                return False


def insertData(db, table, rows, *data):
        cur = db.cursor()
        tmp = ""
        tmp2 = ""
        if (len(rows) != len(data)):
                print(f"\x1b[1;31mError de longitud de datos para tabla {table}")
                return False
        for i in rows:
                tmp += f"`{i}`"
                if i != rows[len(rows)-1]:
                        tmp += ", "
        for i in data:
                if type(i) is int or type(i) is float:
                    tmp2 += f"{i}"
                else:
                    tmp2 += f"'{i}'"
                if i != data[len(data)-1]:
                        tmp2 += ", "
        query = f"INSERT INTO {table} ({tmp}) VALUES ({tmp2});"
        cur.execute(query)
        db.commit()
        cur.close()
        return True

