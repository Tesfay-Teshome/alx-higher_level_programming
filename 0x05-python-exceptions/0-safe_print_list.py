#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for safeprint in range(0, x):
            print(my_list[safeprint], end="")
    except IndexError:
        counter = 0
        for safeprint in my_list:
            counter += 1
        return counter
    else:
        return x
    finally:
        print(end="\n")
