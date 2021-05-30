#This program is an example for while loop
#The script generates a random number between 1 to 1 and lets the user guess the number, page 81 in edureka module 1 presentation 
import math
import random
number=random.randint(1,15)
#print(number)
input_number=int(input("Guess the number in range 1 to 15:"))
while(number!=input_number): #typecasting to int is mandatory because input() returns str type variable and the loop fails 
    if (input_number>number):
        input_number=int(input("Number too big, try again:"))
    elif (input_number<number):
        input_number=int(input("Number too small, try again:"))
print("Good guess! The number is", number)

