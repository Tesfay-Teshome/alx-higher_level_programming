#!/usr/bin/python3
""" Get all states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT states.id, name FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
