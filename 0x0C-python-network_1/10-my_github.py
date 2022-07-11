#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
"""

import requests
import sys

if __name__ == "__main__":
    """
    importing url
    """
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print('{}'.format(req.json().get('id')))
