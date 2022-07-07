#!/usr/bin/python3
import os
import sys
from sys import argv
import urllib.request as request
import requests
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
# retrieving the request
    req = requests.get('https://intranet.hbtn.io/status')
    text = req.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))