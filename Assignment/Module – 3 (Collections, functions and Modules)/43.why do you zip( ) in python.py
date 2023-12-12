# 1). Why Do You Use the Zip () Method in Python ?

# Use of Zip () method in python:
"""
Python's zip() function creates an iterator that will aggregate elements from two or more iterables. 
You can use the resulting iterator to quickly and consistently solve common programming problems, like creating dictionaries.
Syntax :  zip(*iterators) 
Parameters : Python iterables or containers ( list, string etc ) 
Return Value : Returns a single iterator object, having mapped values from all the 
containers.
Zipped (compressed) files take up less storage space and can be transferred to other computers more quickly than uncompressed files.
"""



a = ("harsh", "Twinkle", "Vishvam")
b = ("Gohil", "Gohil", "Rathod", "Krish")

x = zip(a, b)

# Use the tuple() function to display a readable  result:

print(tuple(x))

# Uses types of collection here :

print("\n")
name = [ "harsh", "Sandeep", "Sujit", "Jaydeep" ]
roll_no = [ 13, 15, 18, 7 ]
 
x = zip(name, roll_no)
 
print(set(x))