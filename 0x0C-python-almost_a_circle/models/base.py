#!/usr/bin/python3
'''
the Base imports to the square and the rectangle files
'''

import csv
import json

'''
python libraries imported for class Base
'''

class Base:
    '''import models.base from Base'''
    __nb_objects = 0
    '''a private class attribute
        this manages all the id attributes
        to avoid monotany!!
    '''
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        this is a static dictionary and list
        aka json string
        '''
                    
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        cleverly writes json string representation to a file
        '''
        filename = cls.__name__ + ".json"
        fable = []
        if list_objs is not None:
            for i in list_objs:
                fable.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(fable))

    @staticmethod
    def from_json_string(json_string):
        ''' returns a static list for
        the sake of json string rep
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        '''the instance that returns all attributes
            in which are already set
        '''
        if cls.__name__ is "Rectangle":
            xyz = cls(1, 1)
        elif cls.__name__ is "Square":
            xyz = cls(1)
        xyz.update(**dictionary)
        return xyz
