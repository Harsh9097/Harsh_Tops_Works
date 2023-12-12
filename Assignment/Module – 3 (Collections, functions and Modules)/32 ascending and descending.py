"""
Write a Python script to sort (ascending and descending) a dictionary by
value. 

"""
import operator

d = {1:4,2:6,3:0,4:1,5:2,6:3}

print(d)
print("\n")
sort_d = sorted(d.items(),key = operator.itemgetter(1))
print(sort_d)
print("\n")
sort_d = sorted(d.items(),key = operator.itemgetter(1),reverse = True)
print(sort_d)