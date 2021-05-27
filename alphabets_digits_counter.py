#This program will accept a sentence and cunt the number of letters and digits in it
input_string=input()
number_of_alphabets=0
numer_of_digits=0
for letter in input_string:
    if(letter.isalpha()==True):#check for alphabets
        number_of_alphabets=number_of_alphabets+1
    if(letter.isdigit()==True):#check for digits
        number_of_digits=numer_of_digits+1
print("number_of_alphabets=", number_of_alphabets, "number of digits=", number_of_digits)