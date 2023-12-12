"""
3)Write a Python program to append text to a file and display the text. 
"""

f = open("2.read.txt","a")

name = input("Enter your name :")

f.write("\n"+name)
f.close()