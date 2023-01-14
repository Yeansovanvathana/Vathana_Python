from itertools import product
def all_passwords(chars, length):
    result = []
    chars = "".join(sorted("".join(set(chars))))
    for password in product(chars, repeat = length):
        result.append("".join(password))
    return result

print(all_passwords("abcd", 3))