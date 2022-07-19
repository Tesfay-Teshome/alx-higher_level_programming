#!/usr/bin/python3


def magic_calculation(a, b):
    cal = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                cal += a ** b / i
        except Exception:
            cal = a + b
            break
    return cal
