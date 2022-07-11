#!/usr/bin/python3

"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
from requests import get
import requests


if __name__ == '__main__':

    read= requests.get('https://intranet.hbtn.io/status')
    """ reading and printing"""
    print("Body response:")
    print("\t- type: {}".format(type(read)))
    print("\t- content: {}".format(read))
