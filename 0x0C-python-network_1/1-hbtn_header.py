#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
"""


from nturl2path import url2pathname


if __name__ == "__main__":
    import urllib.request as imports
    from sys import argv
    # x-request-id
    url = argv[1]
    xyz = imports.Request(url)
    with imports.urlopen(r) as response:
        print(response.headers.get('X-Request-Id'))