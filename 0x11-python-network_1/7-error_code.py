#!/usr/bin/python3
""" Takes in a URL, sends a request and displays the body
of the response
if the HTTp status code is >= 400 print Error code
followed by the value of the HHTP status code"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code; {}".format(res.status_code))
    else:
        print(res.text)
