#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    try:
        content = "email=" + urllib.request.quote(email)
        content = content.encode('utf-8')
        req = urllib.request.Request(url, content)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
    except Exception as e:
        print('Error code: ', e.code)
