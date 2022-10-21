#!/usr/bin/python3
""" Search API """

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    try:
        r = requests.post(url, data)
        js = r.json()
        if not js:
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except ValueError:
        print("Not a valid JSON")
