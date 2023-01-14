n = int(input())
arr = list(map(str, input().split()))
B = arr[:len(arr)//2]
C = arr[len(arr)//2:]
print(B, C)
Alice = []
for i in B:
    if i != '0':
        Alice.append(i)
    else:
        Alice.append('')
while '' in Alice:
    Alice.remove('')
print(Alice)
print(len(Alice))
Bob = []
for i in C:
    if i != '0':
        Bob.append(i)
    else:
        Bob.append('')
while '' in Bob:
    Bob.remove('')
print(Bob)
print(len(Bob))
if n > 0:
    if len(B) == len(C):
        print(len(Alice), len(Bob))
        if len(Alice) > len(Bob):
            print("Alice")
        elif len(Bob) > len(Alice):
            print("Bob")
        else:
            print("Draw")
    else:
        Alice = len(Alice) + 1
        Bob = len(Bob) - 1
        print(Alice, Bob)
        if Alice > Bob:
            print("Alice")
        elif Bob > Alice:
            print("Bob")
        else:
            print("Draw")

