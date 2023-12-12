"""
58) Write a Python program to read a random line from a file. 
"""

import random

f = open("C:\\Users\\hk\\OneDrive\\Documents\\GitHub\\harsh-tops-work\\Python_Language\\Assignments\\Module_3-Collections,Functions and Modules\\Read.txt",'r')

lines = f.read().splitlines() 

print(lines)
print(lines[0])

print(random.choice(lines))