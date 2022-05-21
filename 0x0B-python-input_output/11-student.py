#!/usr/bin/python3
'''no module, just class'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''the student, return the self'''
    def to_json(self, attrs=None):
        '''
        function attrs list of strings, attr_names
        '''
        if type(attrs) is list and all([type(xyz) == str for xyz in attrs]):
            return {a: b for a, b in self.__dict__.items() if a in attrs}
        else:
            '''returns the dict of student'''
            return self.__dict__.copy()
    def reload_from_json(self, json):
        '''
        attributes loading from to_json
        '''
        for key, value in json.items():
            '''the writeable public key/val attributes
            '''
            self.__dict__[key] = value
