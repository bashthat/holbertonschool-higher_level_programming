#!/usr/bin/python3
"""
networking! fetching https://intranet.hbtn.io/status
"""

from asyncore import read


if __name__ == "__main__":
    
    import urllib.request as xyz
    url = xyz.Request('https://intranet.hbtn.io/status')
    with xyz.urlopen(url) as response:
        content = xyz.read()
        #reading to print the response
        #retrieving the content
        
        reads = response.read()
        print(f"Body response:")
        print(f"\t- type: (type(reads))")
        print(f"\t- content: {reads})")
        print(f"\t- utf8 content: {reads.decode('utf-8')}")