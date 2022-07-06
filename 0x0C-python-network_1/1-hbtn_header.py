#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
"""


import urllib.request
import sys
import os

#creating the process
#

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as response:
        print(response.getheader("X-Request-Id"))