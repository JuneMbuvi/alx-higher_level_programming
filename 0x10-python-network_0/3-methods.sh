#!/bin/bash
#script that takes in a URL and displays all HTTP methods of the server
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
