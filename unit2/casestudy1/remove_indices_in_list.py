'''
Script removes 0th, 4th and 5th elements from the given list using list comprehensions
'''
x=[12,24,35,70,88,120,155]
x_=[i for i in x if x.index(i) not in {0,4,5} ]
print(x_)
