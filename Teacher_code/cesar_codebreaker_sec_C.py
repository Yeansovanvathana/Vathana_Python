# Brute Force Attack on Cesar Cipher (shift is fixed at 3)/ Simple Substitution Cipher

def decrypt(cipher_text , shifts):

    plain = "" #return value - string that was attempted to be decrypted

    for char in cipher_text:

        if(char.islower()): #Decryption for lower case characters 

            plain += chr((ord(char) - shifts - ord('a')) % 26 + ord('a'))

        elif(char.isupper()): #Decryption for upper case characters

            plain += chr((ord(char) - shifts - ord('A')) % 26 + ord('A'))

        elif(char.isdigit()): #Decryption for digits

            plain += chr((ord(char) - shifts - ord('0')) % 10 + ord('0'))

        else: #Decryption for special Characters like space , /, % etc

            plain += chr((ord(char) - shifts - ord(' ')) % 15 + ord(' '))

    return plain


cipher_text = input("Enter the Cipher Text : ")

#Write a for loop that calls a function called decrypt that would try various permutations of shifts
#and would eventually crack the cipher

for shifts in range(1 , 26):

    plain_text = decrypt(cipher_text , shifts)

    print()

    print("Shift No. " + str(shifts) + " --> " + plain_text)
