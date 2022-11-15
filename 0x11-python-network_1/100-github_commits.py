#!/usr/bin/python3
""" Time for an interview """

if __name__ == "__main__":
    from requests import get, auth
    import sys
    repo = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    r = get(url)
    try:
        js = r.json()
        for j in js[:10]:
            author, name = None, None
            # date = None
            sha = j.get('sha')
            commit = j.get('commit')
            if commit:
                author = commit.get('author')
                # message = commit.get('message')
            if author:
                name = author.get('name')
                # date = author.get('date')
            print("{}: {}".format(sha, name))
    except ValueError:
        print("Not a valid JSON")
