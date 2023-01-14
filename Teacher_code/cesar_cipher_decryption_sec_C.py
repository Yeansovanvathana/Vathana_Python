#Decryption of Cesar Cipher / Substitution Cipher
#Encryption : (P + S) mod 26 = O/P : Cipher Text (C)
#Decryption : (C - S) mod 26 = O/P : Plain Text (P)

#Program to implement decryption process

import string

cipher_text = input("Enter the Cipher Text : ")

shifts = int(input("Enter the Shifts : "))

plain_text = ""

#take each character of cipher text entered by the user & decrypt it
#append it to the plian_text

for char in cipher_text:

    if(char.islower()): #Decryption for lower case characters 

        plain_text += chr((ord(char) - shifts - ord('a')) % 26 + ord('a'))

    elif(char.isupper()): #Decryption for upper case characters

        plain_text += chr((ord(char) - shifts - ord('A')) % 26 + ord('A'))

    elif(char.isdigit()): #Decryption for digits

        plain_text += chr((ord(char) - shifts - ord('0')) % 10 + ord('0'))

    else:

        plain_text += chr((ord(char) - shifts - ord(' ')) % 15 + ord(' '))

print()

print("The Plain Text is : " + plain_text)







        
        













        
