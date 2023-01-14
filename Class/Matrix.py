# hill algorithm
import numpy as np
# Creating the key matrix n by n : k

dim_ket_matrix = int(input("Enter the dimenstions of the key matrix: "))
row_k = dim_ket_matrix
col_k = dim_ket_matrix

# Entering the value of the key matrix
print("Enter the value of elements matrix : ")
key_matrix = []

# travers the row
for i in range(row_k):
    k = []
    for j in range(col_k):
        k.append(int(input()))
    key_matrix.append(k)

key_matrix = np.array(key_matrix)
print("The key mateix [k] is : ")
print(key_matrix)

# get the plain text
plian_text = input("Enter the plain Text for Encryption : ")
plian_text = plian_text.replace(" ", "")
print("Plain text = ", plian_text)
# convert the plain text to length
print("Length of plain text = ", len(plian_text))

#  Is perfectly divisible by the dim(k) and into a numerical matrix that matches the dimensions of the matrix
while(len(plian_text) % dim_ket_matrix != 0):
    plian_text += 'x'
print("Plaintext is ", plian_text)

# Encryption (E[p],E[k])  = [p] * [k] mod 26 = [c] mxn - Cipher matrix
plian_text_index = []
for char in plian_text:
    plian_text_index .append(ord(char) - ord('a'))
print("Indices of the plain text characters = ", plian_text_index)
# Convert this row vector into a matrix s.t. no. col = no.row of [k]
# no of row the [p]
plian_text_index = np.array(plian_text_index)
rp = int(len(plian_text_index) / dim_ket_matrix)
# no of cols of the [p]
cp = dim_ket_matrix
# Resize the list with dim[p] = (rp,cp)
plian_text_index.resize(rp, cp)
plian_text_matrix = plian_text_index
print("Plain text matrix is ")
print(plian_text_matrix)
if(cp == row_k):
    print("Dim of p and k compatible for Multiplication ")
else:
    print("Dim of p and k incompatible !!!!")


# Hill Encryption : E([p],[k]) = [p][k] mod 26 --> o/p [c]
cipher_text = []
cipher_matrix = np.matmul(plian_text_matrix, key_matrix)

print("The cipher Matrix is : ")
print(cipher_matrix)

print("The [c] after mod 26 : [p][k] mod 26 = [c]")
cipher_matrix = np.mod(cipher_matrix, 26)

print(cipher_matrix)

# convert numerical valuse in the cipher matrix to alphabets equivalent to get the cipher txt.
cipher_text_matrix = []
# no rows [c] = no row of [p]
rc = rp
# no cols [c] = no col of [k]
cc = col_k
for i in range(rc):
    c = []
    for j in range(cc):
        c.append(chr(cipher_matrix[i][j] + ord('a')))
    cipher_text_matrix.append(c)
print("The cipher text matrix is : ")
cipher_text_matrix = np.array(cipher_text_matrix)
print(cipher_text_matrix)

# Get the cipher text from cipher text matrix
cipher_text = ""
for i in range(rc):
    for j in range(cc):
        cipher_text += cipher_text_matrix[i][j]
print("The cipher text is : ", cipher_text)