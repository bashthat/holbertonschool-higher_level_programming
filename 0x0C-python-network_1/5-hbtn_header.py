#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable_X-request-id
"""

import requests
import sys

if __name__ == '__main__':
    """
    function that takes in a URL
    """
    request = requests.get(sys.argv[1])
    print(request.headers.get("X-Request-Id"))
