#!/usr/bin/python3
"""new track on model_state"""

from enum import unique
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State

"""
Declarative bass. the Class State.
"""
Base = declarative_base()

class State(Base):
    """
    the base state
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)