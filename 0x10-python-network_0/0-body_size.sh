#!/bin/bash
# Takes in a url, sends a request to that Url
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
