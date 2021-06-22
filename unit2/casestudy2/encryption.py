'''
Script does,
take Username, passcode (length 4, only numbers) and alphanumeric RefID of length 12 as input
Encrypt the RefID using username and password and print the encrypted data
Allow decryption of RefID by the user

Input:
Username (No check)
Passcode (Passcode check for valid passcode with numbers only)
RefID (similarly,check authenticity) - (Dont save RefID directly, Only store Encrypted_RefID)
Output:
Encryption algorithm: Each letter of Encrypted_RefID =  sum of (rand1*first 2 digits of passcode, rand2*last 2 digits of passcode)+(corresponding letter of refID incremented by rand3)
Store rand1, rand2 and rand3 along with Username, password and Encrypted REfID
Print Encrypted_RefID, Ask if encyption is enough? or do you want to decrypt and print the original Ref_ID
Decryption formula: Each letter of Ref_ID = Corresponding letter of Encrypted_RefID -  sum of (rand1*first 2 digits of passcode, rand2*last 2 digits of passcode)
'''
import random
username=input("Enter Username:")
#ref_id=input("Enter your RefID:")
rand_int=[]
invalid=True
while invalid:
    passcode=input("Enter valid passcode:")
    if passcode.isdigit() == False:
        print("invalid passcode, choose a valid passcode")
        invalid = True
        continue
    invalid = False

invalid=True
while invalid:
    ref_id=input("Enter your RefID:")
    if ref_id.isalnum()==False:
        print("invalid RefID, Enter proper RefID")
        invalid = True
        continue
    invalid = False

for i in range(0,3):
    rand_int.append(random.randint(1,10))
#print(rand_int)

#Encrypted_RefID =  sum of (rand1*first 2 digits of passcode, rand2*last 2 digits of passcode)+(corresponding letter of refID incremented by rand3)
enc_id_const=rand_int[0]*int(passcode[0:2])+rand_int[1]*int(passcode[2:3])
inc_id=[]
for i in ref_id:
    inc_id.append(ord(i)+rand_int[2])
#print(inc_id)
enc_id=[]#Encrypted_RefID
for i in inc_id:
    enc_id.append(str(enc_id_const+i))
enc_id="".join(enc_id)
print("Your Encrypted refID is:"+ enc_id) 
