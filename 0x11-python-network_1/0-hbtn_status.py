#!/usr/bin/python3
"""script that fetches a URL"""
import urllib.request


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        content = response.read()

        print("Body Response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
