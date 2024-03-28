#!/usr/bin/python3
"""Manages  urllib.error.HTTPError exceptions and prints: Error code:"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]


    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
