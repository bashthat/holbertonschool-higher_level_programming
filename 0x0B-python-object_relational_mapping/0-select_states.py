#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Creating the SQL table for the list of states in hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == '__main__':

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    charset='utf8',
    )
cursr = db.cursor()
cursr.execute('SELECT * FROM states ORDER BY states.id ASC;')

states = cursr.fetchall()

for x in states:
    print x
cursr.close()
db.close()