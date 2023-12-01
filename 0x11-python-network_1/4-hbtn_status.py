#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
    content = url.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
