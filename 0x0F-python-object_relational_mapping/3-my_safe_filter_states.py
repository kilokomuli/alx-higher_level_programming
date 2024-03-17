#!/usr/bin/python3
""" Takes in 4 arguments and displays all values in the state table where
where name matches the argument and safe from MySQL injections
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    for state in c.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    db.close()
