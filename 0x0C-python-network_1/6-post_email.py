#!/usr/bin/python3
"""
Python script that takes in a URL and an email
and finally displays the body of the response.
"""

import requests
import sys

# email is the parameter

if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(req.text)
