#!/usr/bin/python3
""" Response header value """

if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            Xreq = response.info().get('X-Request-Id')
            print(Xreq)

    except:
        pass
