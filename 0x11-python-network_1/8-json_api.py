#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to a url
with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    try:
        r = requests.get(url, data=data)
        r.raise_for_status()

        js_data = r.json()
        if js_data:
            print("[{}] {}".format(js_data['id'], js_data['name']))
        else:
            print("No result")
    except requests.exceptions.HTTPError as e:
        print("No result" if e.r.status_code == 404 else
              f"Error code: {e.r.status_code}")
    except ValueError:
        print("Not a valid JSON")
