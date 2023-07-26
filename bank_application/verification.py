#!/usr/bin/python3
"""functions for verification """


def verify_age(args):
    if args < 2:
        print("too young to register")
        exit()
