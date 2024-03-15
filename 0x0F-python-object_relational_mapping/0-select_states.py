#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa:
# that takes 3 arguments:mysql username, mysql password and database name

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
