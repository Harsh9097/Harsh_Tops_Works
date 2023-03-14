list1=[1,2,3,4,5]
list2=[1,7,8,9,2]
result = 0
def find_common(list1,list2):
    for x in list1:
        for y in list2:
            if x == y:
                result=True
                return result
            else:
                result=False
                return result

print(find_common(list1,list2))