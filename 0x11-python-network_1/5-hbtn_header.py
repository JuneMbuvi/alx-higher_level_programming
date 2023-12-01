#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if 'X-Request-Id' in req.headers:
        x_request_id = req.headers['X-Request-Id']
        print(x_request_id)
