#!/usr/bin/python3
""" Takes in a URL, sends a request and displays the body
of the response
if the HTTp status code is >= 400 print Error code
followed by the value of the HHTP status code"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code; {}".format(r.status_code))
    else:
        print(r.text)
