'''
this program,
    takes user name and password as input
    cheks the password for criterion in the question
    Promts user if the password is ok
'''

str_name=input("Enter username:")
str_pass=input("Enter password:")
count_uppercase=0
count_lowercase=0
count_digits=0
count_specialchars=0

if len(str_pass)>5 and len(str_pass)<13:#checking length of password
    for letter in str_pass:
        if letter.isupper():#check for upper case letter
            count_uppercase=count_uppercase+1
        elif letter.islower():
            count_lowercase=count_lowercase+1
        elif letter.isdigit():
            count_digits=count_digits+1
        elif letter=="$" or letter=="#" or letter=="@":
            count_specialchars=count_specialchars+1

if count_uppercase==0 or count_lowercase==0 or count_specialchars==0 or count_digits==0:
    print("Invalid password")
else:
    print("Valid password")
    