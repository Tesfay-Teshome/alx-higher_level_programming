#!/usr/bin/python3
""" Defines an object that attribute for lookup function."""


def loockup(obj):
    """ Return a list of an object's available attributes."""
    return (dir(obj))
