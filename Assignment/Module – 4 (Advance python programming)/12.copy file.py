"""
12)Write a Python program to copy the contents of a file to another file. 
"""

f1= open("2.read.txt",'r')
f2= open("sample.txt",'w')

for line in f1:
    f2.write(line)