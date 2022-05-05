#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        theAnswer = a / b
    except ZeroDivisionError:
        theAnswer = None
    finally:
        print("Inside result: {}".format(theAnswer))
        return theAnswer
