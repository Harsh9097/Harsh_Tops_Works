"""
6)Write a Python program to read a file line by line and store it into a list
"""
f=open("2.read.txt","r")

lines = f.readlines()
print(lines)

lines = [x.strip() for x in lines]
print(lines)

