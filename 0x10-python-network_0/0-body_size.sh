#!/bin/bash
#script that takes in a URL, sends a request to that URL & displays body size

curl -sI "$1" | grep -i Content-Length | cut -d " "  -f 2
