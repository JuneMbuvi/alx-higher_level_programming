#!/bin/bash
#Bash script that takes in a URL as an argument, sends a GET request to the URL
curl -s "$1" -H "X-School-User-Id: 98"
