#!/usr/bin/python3
import requests
from urllib import request, error
from sys import argv
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
# retrieving the request

    req = requests.get('https://intranet.hbtn.io/status')
    text = req.text
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))