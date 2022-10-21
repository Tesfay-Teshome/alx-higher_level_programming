#!/usr/bin/python3
""" POST an email """

if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        values = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            Xreq = response.read().decode('utf-8')
            print(Xreq)

    except:
        pass
