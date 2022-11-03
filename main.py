from sys import argv
import dbManager as dbm


def start_db():
    db, cur = dbm.createDatabase("mt")
    return db


def start(*argv):
    db = start_db()

    db.close()


if __name__ == "__main__":
    start(*argv)
