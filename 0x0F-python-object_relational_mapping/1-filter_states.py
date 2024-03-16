#!/usr/bin/python3
""" Lists all states with a name starting with N """


import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id LIMIT 2")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
