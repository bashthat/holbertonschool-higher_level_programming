#!/usr/bin/python3

"""
Write a script that lists all states with a name that starts with N in database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

rows = cursor.fetchall()
for x in rows:
    print(x)

cursor.close()
db.close()