import string
import numpy as np
from sympy import *
##Step 1 : Enter the correct Key Matrix (nxn) - sqr. Matrix - [K] for Decryption
dim_key_matrix = int(input("Enter the dimesion of the KEY MATRIX [K] : "))
rk = dim_key_matrix #no. rows of the [K]
ck = dim_key_matrix #no. col of [K]
key_matrix = []
#Populate the key matrix row wise
print()
print("Enter the elements of the KEY MATRIX [K] row wise : ")

for i in range(rk):
    k = []
    for j in range(ck):
        k.append(int(input()))
    key_matrix.append(k)
print()
print("The Key Matrix [K] is : ")
print()
print(key_matrix)
print()

cipher_text = input("Enter the cipher text C : ")
print()
cipher_text = list(cipher_text)
print("Cipher Characters = ", cipher_text)
print()
cipher_text_index = []
for char in cipher_text:
    cipher_text_index.append(ord(char) - ord('a'))
print("The numerical index of cipher text characters is: ")
print()
print(cipher_text_index)

cipher_text_matrix = np.array(cipher_text_index)
rc = int(len(cipher_text_index) / dim_key_matrix)
cc = rk
cipher_text_matrix.resize(rc, cc)
print("Cipher Matrix : ")
print()
print(cipher_text_matrix)
print()

det_key_matrix = np.mod(int(np.linalg.det(key_matrix)), 26)

print()
print("Determinant of [K]: ", det_key_matrix)
print()

K = Matrix(key_matrix)
adj_key_matrix = np.mod(K.adjugate(), 26)
print("Adj[K] mod 26 = ")
print()
print(adj_key_matrix)
print()

x = 0
while( (det_key_matrix * x) % 26 != 1 % 26):
    x = x + 1
print("The Multiplicative Inverse of |K|^-1 : ", x)
print()

inv_key_matrix = np.mod(np.matmul(x * adj_key_matrix), 26)
print("Inverse of the Key Matrix [K] = ")
print()
print(inv_key_matrix)
print()
print("Test of Invertibility : ")
I = np.mod(np.matmul(key_matrix , inv_key_matrix) , 26)
print(I)
