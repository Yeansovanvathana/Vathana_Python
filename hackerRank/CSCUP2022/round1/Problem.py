n = int(input())
lisA = []
lisB = []
for i in range(n):
    a, b = map(int, input().split())
    lisA.append(a)
    lisB.append(b)
for i in lisA:
    for j in lisB:
        if i > j:
            print("No")
            break
print("Yes")
