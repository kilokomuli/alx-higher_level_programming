#!/usr/bin/python3
""" Takes the name of a state as an argument and lists all cities of
that state"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [sys.argv[4]])
    j = []
    for cities in c.fetchall():
        j.append(cities[1])
    print(", ".join(j))
    c.close()
    db.close()
