#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except urllib.error.URLError as e:
        print(e.reason)
