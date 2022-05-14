#!/usr/bin/python3
'''this function states a first and last name through a series of exmaples and tests.'''



def say_my_name(first_name, last_name=""):


    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {} ".format(first_name, last_name))
