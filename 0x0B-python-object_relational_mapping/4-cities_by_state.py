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
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC")

    states = cursor.fetchall()

    for row in states:
        print(row)
    cursor.close()
    db.close()