#!/usr/bin/python
# -*- coding: utf-8 -*-

"""a script that prints the first State object from the database hbtn_0e_6_usa"""

if __name__ == '__main__':

    import sys
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv
    from model_state import Base, State

    engine = \
        create_engine('mysql+mysqldb;//{}:{}@localhost/{}'.format(sys.argv[1],
                      sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    """
    model 
    """
    session = Session(engine)
    first = session.query(State).order_by(State.id).first()
    if first:
        print ("{}: {}".format(first.id, first.name))
        """
        if __table__ states is nothing, print 'nothing'
        """
    else:
        print ('Nothing')
    session.close()