#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        access_token = sys.argv[2]

    auth = {username, access_token}
    url = "https://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"
    try:
        r = requests.post(url, auth=auth)
        r.raise_for_status()

        j_data = r.json()

        if 'id' in j_data:
            print(j_data['id'])
        else:
            print("None")
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.r.status_code}")
    except ValueError:
        print("Not a valid JSON")
