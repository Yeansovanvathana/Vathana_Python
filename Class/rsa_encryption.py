#RSA ENCRYPTION BATCH B9

#Step 2 : Encryption : (M^e) mod n = C ; M = PT ; C = CT

# E(M , e , n) = C ; {e , n} = Pub. Key of Receiver

print()

M = input("Enter the message to be encrypted : ")

print()

print("Enter the Public Key { e , n } of the Receiver : ")

e = int(input("Enter the value of [e] : "))

n = int(input("Enter the value of [n] : "))

print()

#Encryption Happens here: (M^e) mod n = C ; M = PT ; C = CT

C = ""

for char in M :

    C += chr(pow(ord(char), e, n))

print()

print("The Cipher Text C = M^e mod n = ["+C+"]")