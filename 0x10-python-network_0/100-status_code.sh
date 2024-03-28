#!/bin/bash
# Display only status cone sends a requets to URL passed as an argument
curl -L -s -X HEAD -w "%{http_code}" "$1"
