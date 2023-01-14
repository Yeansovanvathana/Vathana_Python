# cipher_text_key = ['g', 'z', 'b', 'f', 'c', 'x', 'q', 'r', 'v', 's', 'd', 'w', 't', 'u', 'a', 'l', 'm', 'n',
#               'k', 'j', 'i', 'y', 'e', 'o', 'h', 'p']

key = 'gzbfcxqrvsdwtualmnkjiyeohp'

def encrypt(cipher_text, key):
    text = ''
    for char in cipher_text:
        if (char.islower()):
            index = ord(char) - ord('a')
            text += key[index]
        else:
            text += char
    return text

cipher_text = input("Enter the cipher_text: ")
plain_text = encrypt(cipher_text, key)
print('The plain text is: ' + plain_text)