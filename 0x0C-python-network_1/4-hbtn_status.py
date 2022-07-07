#!/usr/bin/python3
import requests

"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':

    # retrieving the request

    rx = requests.get('https://intranet.hbtn.io/status')
    read = rx.text
    print("Body response:")
    print("\t- type: {}".format(type(read)))
    print("\t- content: {}".format(read))
