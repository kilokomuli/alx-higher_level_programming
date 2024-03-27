#!/bin/bash
# sends a JSON POST request
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
