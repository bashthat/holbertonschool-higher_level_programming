#!/usr/bin/python3
"""
networking! fetching https://intranet.hbtn.io/status
"""


import urllib.request


def fetcher():
    
    
if __name__ == "__main__":    
    """
    fetching the request.
    """
    import urllib.request as xyz
        request = xyz.request ("https://intranet.hbtn.io/status")
        with xyz.urlopen(request) as response:
        """
        reading to print the response
        """
        site = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))


    fetcher()