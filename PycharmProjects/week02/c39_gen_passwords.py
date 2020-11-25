import random
def gen_passwords(chars, length, number):
    lis = []
    for i in range(number):
        password = ""
        for x in range(length):
            password += random.choice(chars)
        lis.append(password)
    return lis
print(gen_passwords("abc123", 5, 3))