#!/bin/bash
#Takes in URL as an argument, sends GET request, Dispalys body of the response
curl -s -H "X-School-User-Id: 98" "$1"
