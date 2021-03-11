#!/usr/bin/env python3

"""
https://docs.python.org/3/tutorial/
"""

import sys


def number():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)


def arg_func():
    if __name__== "__main__":
        print(sys.argv)
        i=1
        while i < len(sys.argv):
            print(sys.argv[i])
            i += 1

class person:
    # pass does nothing, use as a stub
    pass

num = 5
print("num location is: %x" % id(num))
print("num initially is: %i" % num)


def change_external(var):
    """ Observe local symbol table and memory addresses
    """
    print("num location in func: %x" % id(var))
    print("loaded number is %i" % var)
    var += 5
    print("changed num location is: %x" % id(var))
    print("changed number is %i" % var)


if __name__ == "__main__":
    #Evan = person()  # creates a person object called Evan
    #print(Evan)   # shows symbol table and type at memory location for object
    #print(arg_func)

    # See change_external() 
    change_external(num)
    print("num location after, in main is: %x" % id(num))
    print("num after, in main is: %i" % num)