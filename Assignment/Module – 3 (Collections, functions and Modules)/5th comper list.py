"""
5) How will you compare two lists? 

Using list.sort() and == operator :
-->> The list.sort() method sorts the two lists and the == operator compares the two lists item by item which means they have equal data items at equal positions. 
    This checks if the list contains equal data item values but it does not take into account the order of elements in the list. 
            This means that the list [1,2,3] will be equal to the list [2,1,3] according to this method of comparison.
"""
# Compare Two lists syntax :

list1 = [10, 20, 30, 40, 50, 60]  
list2 = [10, 20, 30, 50, 40, 60]  
   
# Sorting the list  
list1.sort()  
list2.sort()    
  
if list1 == list2:  
    print("The list_1 and list_2 are the Equal")  
else:  
    print("The list_1 and list_2 are not the Equal")  
  