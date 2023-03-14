"""
9)Write a Python program to count the number of lines in a text file. 
"""

# Open the file for reading
with open('2.read.txt', 'r') as file:
  
    line_count = 0
 
    for line in file:
      
        line_count += 1


print("Total number of lines:=====>", line_count)