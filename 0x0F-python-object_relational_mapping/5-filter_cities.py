#!/usr/bin/python3
""" Takes the name of a state as an argument and lists all cities of
that state"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
               passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    for cities in c.fetchall():
        if cities[4] == sys.argv[4]:
            print(", ".join([cities[2]]))
    c.close()
    db.close()
