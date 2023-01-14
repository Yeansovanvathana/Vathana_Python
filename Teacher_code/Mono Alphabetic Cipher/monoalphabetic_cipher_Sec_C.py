#Implementation of Mono Alphabetic / Permutation Cipher Technique
#Summary : For ever Plain Text Character there is a unique but totally random assignment of cipher text

import string
import random

def create_key():

    english_alphabets = string.ascii_lowercase
    print("English Alphabets : " + english_alphabets)
    print()

    atoz_list = list(english_alphabets)

    random.shuffle(atoz_list)

    key1 = "".join(atoz_list)

    return key1

#Encryption Function

def encrypt(plain_text , key):

    cipher = ""

    for char in plain_text:

        if(char.islower()):

            index = ord(char) - ord('a') # value between 0-25
            cipher += key[index]

        elif(char.isupper()):

            index = ord(char) - ord('A')
            cipher += key[index]

        else:

            cipher += char


    return cipher

#Decryption Function

def decrypt(cipher_text , key):

    plain = ""

##Step 3 : for all char in the cipher_text
## index = (index of the char in the key)
##append(plain_text , chr(index + ascii(‘a’)

    for char in cipher_text:

        if(char.islower()):

            index = key.find(char)

            plain += chr(index + ord('a'))

        else:

            plain += char


    return plain
    

#Step 1 : Create the random key for encryption

key = create_key()
print("The Random Key Generated is : " + key)

#Step 2 : Get the plain text for encryption

plain_text = input("Enter the plain Text : ")

#Step 3 : Encrypt the plain text and generate the ciphertext

cipher_text = encrypt(plain_text , key)

print()
print("The Cipher Text is : " + cipher_text)

#step 4 : Decryption Process
##Step 1 : Get the Cipher Text
##Step 2 : Enter the correct Key
# Call function decrypt

original_message = decrypt(cipher_text , key)

print("The decrypted Plain Text is : " + original_message)

#Logic for encrupting digits 


















