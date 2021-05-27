#this program chcks input number for palindrome or not
print("Enter number to check:")
input_number=input()
flag=True
for i in range(len(input_number)):
    if(input_number[i]!=input_number[len(input_number)-i-1]):#check if the number is palindrome
        flag=False#set to false and break
        print("Not a palindrome")
        break
    else:
        flag=True#set to true if palindrome
if flag is True:
    print("the number is a palindrome")#print number if flagis true