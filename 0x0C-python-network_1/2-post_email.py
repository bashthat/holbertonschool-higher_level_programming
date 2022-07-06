#!/usr/bin/python3
""" 
a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter
"""
import email
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    rpost = request.Request(argv[1], data)
    """script displays the body of the response (decoded in utf-8)"""
    with request.urlopen(rpost) as response:
        """script"""
        print(response.read().decode("utf8"))