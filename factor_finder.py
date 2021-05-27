#This function finds the factors of the given number and sorts all the factors into even or odd numbers

import sys
import math

num=input("Enter number to find factors:")#get user input to 
num=int(num)#Type casting to int
num_sqrt=num ** 0.5 # All the factors of a numbers can be obtained within in the square root of that number. improves run time for big numbers.
num_sqrt=math.ceil(num_sqrt) #rounding off to upper number
factors_range=list(range(1,num_sqrt+1))# creating list with all possible left side multiples 
factors=[]
for i in factors_range:
    if num%i==0:
        factors.append(i)
        factors.append(int(num/i))

print("factors of ",num, "are",factors)

for i in factors:
    if i%2==0: print(i, "is even")
    else: print(i, "is odd")