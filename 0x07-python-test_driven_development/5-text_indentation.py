#!/usr/bin/python3

'''this is a test
    Write a function that prints a text
    with 2 new lines after each of these
    characters: ., ? and :
'''


from operator import truediv


def text_indentation(text):
    if type(text) is not str or text =="":
        raise TypeError("text must be a string")
    spec_char = [".", "?", ":"]
    while true:
        for xlt in text:
            if xlt in spec_char:
                print(xlt)
                print()
                print('', end='', flush=True)

            else:
                print(xlt, end="", flush=True)
        break