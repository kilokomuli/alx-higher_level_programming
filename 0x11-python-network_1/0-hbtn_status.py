#!/usr/bin/python3
"""  script that fetches https://alx-intranet.hbtn.io/status
using  package urllib """
import urllib.request


if __name__ = "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()
