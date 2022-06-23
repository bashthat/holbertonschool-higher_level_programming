#!/usr/bin/python3


""" Creating the SQL table for the list of states in hbtn_0e_0_usa """

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
    cursor.execute('SELECT * FROM states ORDER BY states.id;')

    states = cursor.fetchall()

    for x in states:
        print(x)
    cursor.close()
    db.close()