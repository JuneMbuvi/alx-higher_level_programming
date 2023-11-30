#!/bin/bash
#sends a request to a URL passed as an argument & displays the status code
curl -s -L -X HEAD -w "%{http_code}" "$1"
