''' the program does:
take a string intput
print the letters with their number of occurrences 
'''
str_input=input("Enter the string:")
comp_list=set(str_input)
for letter in comp_list:
    #count = 0
    print(letter+','+str(str_input.count(letter)))