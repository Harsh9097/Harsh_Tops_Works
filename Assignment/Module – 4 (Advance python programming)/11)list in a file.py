"""
11)Write a Python program to write a list to a file. 

"""
items = ['Mango', 'Orange', 'Apple', 'Lemon']
f = open("sample.txt",'w')
f.writelines(items)
f.close()