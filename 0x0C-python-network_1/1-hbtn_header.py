#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request.
"""

import urllib
import urllib.request
import sys


# the process
# imporing only urllib.request and sys

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as response:
        print(response.getheader("X-Request-Id"))
