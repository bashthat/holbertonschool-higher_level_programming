#!/usr/bin/python3
"""
a Python script that takes in a URL and an email.
"""

import urllib
import urllib.request as request
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    """taking in url/email"""
    e_mail = {"email": argv[2]}
    rpost = parse.urlencode(e_mail).encode('utf-8')
    req = request.Request(argv[1], rpost)
    """script displays the body of the response (decoded in utf-8)"""
    with request.urlopen(req) as response:
        """script"""
        print(response.read().decode("utf8"))
