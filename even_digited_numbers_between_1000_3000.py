import math
even_digited_numbers=[]
for i in range(1000,3001,2):#step 2 is used, saves run time
    j=int(i)
    while(j!=0):#loop till the number is reduced to zero
        if((j%2)!=0):#break if any digit is odd
            break
        j=math.floor(j/10)#shift the digit right
        if(j==0):#if j is 0 it has all digits even
            even_digited_numbers.append(i)#append to the list of required numbers
print(even_digited_numbers)#print list