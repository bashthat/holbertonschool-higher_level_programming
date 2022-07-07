#!/usr/bin/python3
from urllib import read
import requests
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
# retrieving the request

    r = requests.get('https://intranet.hbtn.io/status')
    read = r.text
    print("Body response:")
    print("\t- type: {}".format(type(read)))
    print("\t- content: {}".format(read))