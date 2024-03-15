#!/usr/bin/python3
""" Takes an argument and displays all values in the states table"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    state = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name LIKE %s", (state, ))
    results = c.fetchall()
    for row in results:
        print(row)
    c.close()
    db.close()
