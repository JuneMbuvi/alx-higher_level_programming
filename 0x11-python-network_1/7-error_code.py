#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get(url)
        req.raise_for_status()

        print(req.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
