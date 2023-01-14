# Cesar Cipher Encryption a special case of Substitution Cipher pin the shift at 3

plain_text = input("Enter the plain text to be encrypted : ")

print()

shifts = int(input("Enter the number of shifts : "))

cipher_text = ""

for char in plain_text:

    if(char.islower()): #character is lowercase

        cipher_text += chr((ord(char) + shifts - ord('a')) % 26 + ord('a'))

    elif(char.isupper()): #character is upper case

        cipher_text +=  chr((ord(char) + shifts - ord('A')) % 26 + ord('A'))

    #Encrypting numbers , special characters

    elif(char.isdigit()): # character is number

        cipher_text +=  chr((ord(char) + shifts - ord('0')) % 10 + ord('0'))
    
    else:

        cipher_text += chr((ord(char) + shifts - ord(' ')) % 15 + ord(' '))


print("Plain Text is : " + plain_text)
print("Cipher Text is : " + cipher_text)






