"""
8)Write a python program to find the longest words.

"""

f = open("2.read.txt","r")


words = f.read().split()
max_len = len(max(words, key = len))
result = [word for word in words if len(word) == max_len]
 
print("Longest Word : ", result)
