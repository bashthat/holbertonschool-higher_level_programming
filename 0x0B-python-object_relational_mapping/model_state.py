#!/usr/bin/python3
"""new track on model_state"""

import sys
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State

Base = wobble_base()

class State(Base):
"""
imports//Base.metadata.create_all(engine)//
"""
    __
   
    Base.metadata.create_all(engine)