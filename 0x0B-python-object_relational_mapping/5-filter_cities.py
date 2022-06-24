#!/usr/bin/python3


""" Creating a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    charset='utf8',
    )
    word = db.cursor()
    word.execute("SELECT cities.name FROM cities LEFT JOIN states ON states.id = cities.state_id WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))

    states = word.fetchall()

    print(" ".join([row[0]] for row in states))
    word.close()
    db.close()