
#from __future__ import print_function
"""
https://docs.python.org/3/howto/argparse.html
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filename", help="Input filename goes here. Positional arg")
parser.add_argument("number", help="This needs to be an int", type=int)

# '-' is the default optional arg prefix in the argparser constructor. - is optional and second '-'
# is part of the name of the argument. Double is convention to allow for short version too.
# But a single would still work if you specified it that way when adding the argument

# Subparsers only have one method, add_parser()

args = parser.parse_args()

print(type(args))
print(args)