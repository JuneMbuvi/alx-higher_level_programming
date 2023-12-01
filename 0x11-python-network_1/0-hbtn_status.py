#!/usr/bin/python3
"""script that fetches a URL"""
import urllib.request


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        pg = response.read()

    print("Body Response:")
    print("\t- type:", type(pg))
    print("\t- content:", pg)
    print("\t- utf8 content:", pg.decode('utf-8'))
