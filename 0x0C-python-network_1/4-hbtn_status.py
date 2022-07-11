#!/usr/bin/python3

"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
from requests import get
import requests


if __name__ == '__main__':

    read = get('https://intranet.hbtn.io/status')
    words = read.words
    """ reading and printing"""
    print("Body response:")
    print("\t- type: {}".format(type(words)))
    print("\t- content: {}".format(words))
