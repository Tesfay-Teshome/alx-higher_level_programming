#!/usr/bin/python3
""" Error Code with Requests """

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    code = r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
