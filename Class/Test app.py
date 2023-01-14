import math as m
p = int(input(""))
q = int(input(""))

f_n = (p - 1)*(q - 1)
print("f_n = ", f_n)
print()

#Public Key = { e, n }
e = 2
public_key_list = []
while (e < f_n):
    if (m.gcd(e, f_n) == 1):
        public_key_list.append(e)
    e = e + 1
print("Public Key list of Receiver: ")
print()
print(public_key_list)
print()

e = int(input("Choose a Public Key [e] from the above list : "))
d = 2
while (d < f_n):
    if ((e*d) % f_n == 1):
        break
    else:
        d += 1
print()
print("The Public Key { e, n} = {", e," , ", n, " }")
print()
print("The Private Key {d, n} = {", d," , ", n, " }")
M = input("Enter the secret message [M] = ")
print()
print ("The Sender Encrypts the Message M as [M^e mod n] = C & Sneds its to the Receiver.")
print ()
C = "" #Cipher Text
for char in M:
      C += chr(pow (ord(char) , e, n))

print("The Cipher Text [C] = ["+C+"]")