#!/usr/bin/env python3
from requests import requests
from requests import get
from sys import argv


"""
Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable_X-request-id
"""

if __name__ == '__main__':
    
    request = get(argv[1])
    print(request.headers.get('X-Request-Id'))