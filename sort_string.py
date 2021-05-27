#program takes a sentence input from user and arranges the words into the order from a to z
'''
ignore these lines
#str="NOJIGK Nihnr fiLKNO IOihnr firuhgp"
#string_validity=isalpha(str)
#if (str.isalpha()|| str.isspace())==False:
#if (!str.isalpha()): does not work, syntax error at "!"
#    print("Enter valid string,alphabets  only")
#print()
#print(str)
#print(str.casefold())
'''
words_input=[]
words_output=[]
word="h"#dummy alphabet initialized
print("Enter words to sort:")
while(word.isalpha()==True):#takes user input words
    word=input()
    words_input.append(word)
words_input=words_input[:-1]# remove the last entry i.e. "carriage return"
print(words_input)#prints all input words
words_output=sorted(words_input)#sorted() function is used to sort the list. sort() did not work for me, for this use case
print(words_output)

'''
for word in words_input:
    word_select=word.casefold()
    #print(word_select[0])
    for word in word_select:
        #print(word[0])
        if (word[0]>word_select[0]):
            sort
'''