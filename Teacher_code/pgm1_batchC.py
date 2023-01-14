#Simple Cryptography Program for encrypting and decrypting a message

#Step 1 : Encryption(Encr) : Encr(plain text , key) = O/P Cipher text

from cryptography.fernet import Fernet

#step1.1 : Create the key

key = Fernet.generate_key() #a random 128 bit key is generated

f = Fernet(key)

print("the secret key is : " + str(key))

#Plain Text / seret message to be encrypted a + b

plain_text = bytes(input("Enter the message to be encrypted : "), 'ASCII')

#Encryption

cipher_text = f.encrypt(plain_text)
print()

print("The Cipher Test is : " + str(cipher_text))

#Step 2 : Decryption (Decr) : Decr(cipher text , key) = O/P Plain text

print("The decrypted cipher text is : " + str(f.decrypt(cipher_text)))








