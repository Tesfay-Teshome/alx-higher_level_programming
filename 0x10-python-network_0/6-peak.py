#!/usr/bin/python3
""" Function to find a peak in list """


def peak_recur(a, Min, Max):
    """ Binary Search Recursion """

    if not a:
        return None

    half = int((Max + Min) / 2)

    if (half - 1) < Min and (half + 1) > Max:
        return a[half]

    if (half - 1) < Min and (half + 1) <= Max and a[half + 1] <= a[half]:
        return a[half]

    if (half + 1) > Max and (half - 1) >= Min and a[half - 1] <= a[half]:
        return a[half]

    if (half - 1) >= Min and a[half - 1] <= a[half] \
       and (half + 1) <= Max and a[half + 1] <= a[half]:
        return a[half]

    if a[half + 1] > a[half]:
        return peak_recur(a, half + 1, Max)

    return peak_recur(a, 0, half - 1)


def find_peak(list_of_integers):
    """ Finds a peak in unsorted array """

    if not list_of_integers:
        return None

    Min = 0
    Max = len(list_of_integers) - 1

    return peak_recur(list_of_integers, Min, Max)
