#!/bin/bash
# Takes in URl, sends a get request and dispalys body response
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
