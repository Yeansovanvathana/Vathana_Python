n = int(input())
arr = list(map(str, input().split()))
# arr = "".join(arr)
# firstpart, secondpart = arr[:int(len(arr)/2)], arr[int(len(arr)/2):]
# print(firstpart, secondpart)
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
firstpart = Convert(firstpart)
secondpart = Convert(secondpart)
print(firstpart, secondpart)
Alice = []
for i in firstpart:
    if i != '0':
        Alice.append(i)
    else:
        Alice.append('')
print(Alice)
Bob = []
for i in secondpart:
    if i != '0':
        Bob.append(i)
    else:
        Bob.append('')
print(Bob)
if n > 0:
    if len(Bob) > len(Alice):
        Alice = "".join(Alice).split("''")
        Bob = "".join(Bob).split("''")
        Alice = "".join(Alice)
        Bob = "".join(Bob)
        Alice = len(Alice) + 1
        Bob = len(Bob) - 1
        print(Alice, Bob)
        if Alice > Bob:
            print("Alice")
        elif Bob > Alice:
            print("Bob")
        else:
            print("Draw")
    elif len(Bob) == len(Alice):
        print(Alice, Bob)
        if len(Alice) > len(Bob):
            print("Alice")
        elif len(Bob) > len(Alice):
            print("Bob")
        else: print("Draw")


