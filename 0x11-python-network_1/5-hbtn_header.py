#!/usr/bin/python3
""" Response header with requests """

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    Xreq = r.headers.get('X-Request-Id')
    print(Xreq)
