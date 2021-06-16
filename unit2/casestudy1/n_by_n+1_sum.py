'''
Script generates n/n+1 sum for the given number
'''
number=int(input("Enter n to generate n/n+1 sum:"))
sum=0
for i in range(1,number+1):
    sum+=i/(i+1)
print(sum)