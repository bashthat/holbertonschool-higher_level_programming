#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""new track on model_state"""

from enum import unique
import sys
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State

Base = declarative_base()


class State(Base):

    """
    the base state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)