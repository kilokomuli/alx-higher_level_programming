#!/bin/bash
# Displays all HTTP methods server will accept
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
