#!/usr/bin/python3
""" POST an email with requests """

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    r = requests.post(url, data)
    body = r.text
    print(body)
