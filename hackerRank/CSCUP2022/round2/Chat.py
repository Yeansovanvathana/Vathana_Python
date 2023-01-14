from collections import OrderedDict
def checkOrder(string, pattern):
    dic = OrderedDict.fromkeys(string)
    ptr = 0
    for key, value in dic.items():
        if (key == pattern[ptr]):
            ptr = ptr + 1
        if (ptr == (len(pattern))):
            return 'YES'
    return 'NO'

string = input()
pattern = 'helo'
print(checkOrder(string, pattern))

