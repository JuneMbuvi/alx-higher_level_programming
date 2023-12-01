#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    req = requests.post(url, data=data)
    print(req.text)
