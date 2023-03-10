# 1). Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print("Unique elements are : ")
print(unique_list([1,2,4,5,4,5,6,9,10]))


"""
def get_uniqList(inputList):
       print('Unique List Is : ',[*set(inputList)]) 
a =  [1,2,5,1,8,5,2,6,5,9,26,22,1,1,1,1]
uniq = get_uniqList(a)
"""