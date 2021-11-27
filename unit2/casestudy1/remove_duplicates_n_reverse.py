'''
Script removes duplicate elements and reverses the resulting list
'''
list1=[12,24,35,24,88,120,155,88,120,155]
list1=[i for i in list1 if (list1.count(i)==1)]#Could not use set() to remove duplicates as it will mess up the original order of the list
list1.reverse()# Observation: Returns None, so print in the next line haha! 
print(list1)
#list1=[i for i in reversed(list1)] --> another way to reverse the list
