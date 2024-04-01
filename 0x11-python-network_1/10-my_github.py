#!/usr/bin/python3
"""Sends a search request for a given string to the Star
The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    result = requests.get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
