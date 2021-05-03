"""
https://docs.python.org/3/tutorial/inputoutput.html
"""

year = 2021
name = 'Evan'

#f for formatted string literal
# {} squigly brackets
print(f'My name is {name} and the year is {year}')

# The str() function is meant to return representations of values which are 
# fairly human-readable, while repr() is meant to generate representations
# which can be read by the interpreter.

# Open file in read-and write
f = open('filename.txt', 'r+')
f.close()

# Read in binary. Necessary for non-text encoding
f = open('filename.txt', 'rb')

# USE With loop contruct or f.close() after writing, else buffers may not be 
# emptied and you could experience data loss

# running f.read() will pull the entire file, subsequent read() will return ''
f.readline() is another method for these file descriptors

# Go to beginning of the file
f.seek(0)

# Tell me the position of the pointer in the file
f.tell()

# use json module to spill into serialized output
out = json.dump(f)

# use json module to deserialize into a strucutre to work on
working_dict = json.load(f)

# This doesn't work for arbitrary class data, only those that can cleanly
# export to file. For arbitrary complexity, use pickle. NOTE: pickle is
# only safe for Python and is not interop like JSON
