'''
Script generates 5 rand numbers in range 1 and 1000 divisible by both 5 and 7
'''
import random
length=5
set_input=[i for i in range (1,1000) if (i%5==0 and i%7==0)]
print(random.sample(set_input,5))
