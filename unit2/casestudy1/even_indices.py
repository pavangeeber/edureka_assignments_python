'''
This program,
takes string input, converts to list,
iterates through list to remove even indices
joins the resulting list backinto a single string and prints it
'''
str_input=input("Enter the string:")
list1=list(str_input)
i=0
while (i < len(list1)-1):
    list1.pop(i+1)
    i+=1
str_output="".join(list1)
# str_output=str(list1).lstrip("['")
# str_output=str_output.rstrip("']")
print(str_output)
