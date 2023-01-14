#Decryption
import string

cypertext = input('Enter the cypertext: ')
shifts = int(input('Enter the shifts : '))
plain_text = ''

for char in cypertext:

    if (char.islower()):
        plain_text += chr((ord(char) - shifts - ord('a')) % 26 + ord('a'))

    elif (char.isupper()):
        plain_text += chr((ord(char) - shifts - ord('A')) % 26 + ord('A'))

    elif (char.isdigit()):
        plain_text += chr((ord(char) - shifts - ord('0')) % 10 + ord('0'))

    else:
        plain_text += chr((ord(char) - shifts - ord(' ')) % 15 + ord(' '))
print()
print('The plain_text is: ' + plain_text)