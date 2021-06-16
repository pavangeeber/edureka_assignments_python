'''
Script removes elements divisible by both 5 and 7 from the given list using list comprehensions
# Replace 'and' with 'or' on line 6 to remove elements divisible by either 5 or 7 
'''
x=[12,24,35,70,88,120,155]
x_=[i for i in x if (i%5 or i%7)]#Note:bitwise operators '|' won't yield the same result
#check=[5,7]
#x_=[i for i in x for j in check if i%j!=0]
print(x_)