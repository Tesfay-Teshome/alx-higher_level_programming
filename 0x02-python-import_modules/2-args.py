#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    m = len(sys.argv) - 1
    if m == 0:
        print("0 arguments.")
    elif m == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(m))
    for x in range(m):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
