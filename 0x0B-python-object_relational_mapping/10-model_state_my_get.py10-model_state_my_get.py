#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':

    import sys
    import sqlalchemy
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = \
        create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                      sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

for state in session.query(State).filter(State.name
        == sys.argv[4]).first:
    if state:
        print ("{}").format(state.id)
    else:
        print ("Not found")
    session.close()