"""
Write a Python program to convert a list of tuples into a dictionary. 
"""
list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict=dict()
 
for student,score in list_1:
    dict.setdefault(student, []).append(score)
print(dict)