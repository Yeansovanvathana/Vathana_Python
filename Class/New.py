alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ciper_text_key = ['g', 'z', 'b', 'f', 'c', 'x', 'q', 'r', 'v', 's', 'd', 'w', 't', 'u', 'a', 'l', 'm', 'n',
#               'k', 'j', 'i', 'y', 'e', 'o', 'h', 'p']

# key = ''.join(ciper_text_key)
key = 'gzbfcxqrvsdwtualmnkjiyeohp'
print(key)


# ciper_text = 'jx um uj xsov ud vxn lorm mx tnjm auiw nz'
def encrypt(decryte_text, key):
    ciper = ''
    for char in decryte_text:
        if (char.islower()):
            index = key.find(char)
            ciper += chr(index + ord('a'))
        else:
            ciper += char
    return ciper

def decrypt(cipher_text, key):
    text = ''
    for char in cipher_text:
        if (char.islower()):
            index = ord(char) - ord('a')
            text += key[index]
        else:
            text += char
    return text


decrypt_text = input("Enter the plain_text: ")
plain_text = encrypt(decrypt_text, key)
print('The cipher_text is: ' + plain_text)

cipher_text = input("Enter the cipher_text: ")
plain_text = decrypt(cipher_text, key)
print('The plain text is: ' + plain_text)


