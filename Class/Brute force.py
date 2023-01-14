def decrypt(cipertext, shifts):
    plain = ''
    for char in cipertext:
        if (char.islower()):
            plain += chr((ord(char) - shifts - ord('a')) % 26 + ord('a'))

        elif (char.isupper()):
            plain += chr((ord(char) - shifts - ord('A')) % 26 + ord('A'))

        elif (char.isdigit()):
            plain += chr((ord(char) - shifts - ord('0')) % 10 + ord('0'))

        else:
            plain += chr((ord(char) - shifts - ord(' ')) % 15 + ord(' '))
    return plain


ciper_text = input('Enter the ciper text: ')

for shifts in range(1, 26):
    plain_text = decrypt(ciper_text, shifts)
    print(plain_text + ' => shifts: ' + str(shifts))