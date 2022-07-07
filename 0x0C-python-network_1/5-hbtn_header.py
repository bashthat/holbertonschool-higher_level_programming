#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable_X-request-id
"""

import requests

if __name__ == '__main__':
    """
    function that takes in a URL
    """
    request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))