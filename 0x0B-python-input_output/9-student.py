#!/usr/bin/python3
'''no module, just class'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''the student, return the self'''
    def to_json(self):
        return self.__dict__.copy()
