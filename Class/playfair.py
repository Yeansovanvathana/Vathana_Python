import string

english_alphabet = string.ascii_lowercase
english_alphabet = english_alphabet.replace('j', '.')

keyword = input("Enter the keyword: ")
print("The keyword is: ", keyword)

print("Reference String is: ", english_alphabet)
print()

key_matrix = ['' for i in range(5)]
print("Initialised Key matrix : ")
print(key_matrix)
print()

row = 0
column = 0

for char in keyword:
    if char in english_alphabet:
        key_matrix[row] += char
        english_alphabet = english_alphabet.replace(char, '.')
        # print(english_alphabet)
        column = column + 1
        if(column > 4):
            row += 1
            column = 0
print("Key Martix populated only with the key word Characters :")
print(key_matrix)
print()

for char in english_alphabet:
    if (char != "."):
        key_matrix[row] += char
        column += 1

        if(column > 4):
            row = row + 1
            column = 0
print("The final key matrix is: ")
print(key_matrix)
print()

plain_text = input("Enter the plain text: ")
plain_diagram = []
i = 0
plain_text = plain_text.replace(" ", "")
# print(plain_text)
while i < len(plain_text):
    char1 = plain_text[i]
    char2 = ''

    if(i+1) == len(plain_text):
        char2 = 'x'
    else:
        char2 = plain_text[i+1]

    if(char1 != char2):

        plain_diagram.append(char1 + char2)
        i += 2
    else:

        plain_diagram.append(char1 + 'x')
        i += 1

print()
print("The diagaram is: ")
print(plain_diagram)

cipher_text = []

for diagram in plain_diagram:
    applied_rule = False

    for row in key_matrix:
        if (diagram[0] in row and diagram[1] in row):
            col0 = row.find(diagram[0])
            col1 = row.find(diagram[1])

            ct_pair = row[(col0 + 1) % 5] + row[(col1 + 1) % 5]
            cipher_text.append(ct_pair)
            applied_rule = True
    if applied_rule:
        continue

    for j in range(5):
        col = ''.join([key_matrix[i][j] for i in range(5)])
        if(diagram[0] in col and diagram[1] in col):
            row0 = col.find(diagram[0])
            row1 = col.find(diagram[1])

            ct_pair = col[(row0 + 1) % 5] + col[(row1 + 1) % 5]
            cipher_text.append(ct_pair)

            applied_rule = True
    if applied_rule:
        continue

    row0 = 0
    col0 = 0

    row1 = 0
    col1 = 0

    for i in range(5):
        row = key_matrix[i]
        if(diagram[0] in row):
            row0 = i
            col0 = row.find(diagram[0])
        if(diagram[1] in row):
            row1 = i
            col1 = row.find(diagram[1])

    ct_pair = key_matrix[row0][col1] + key_matrix[row1][col0]

    cipher_text.append(ct_pair)

print("The diagram cipher_text: ")
print(cipher_text)

cipher_text = ''.join(cipher_text)
print()
print("The cipher text is: ", cipher_text)


