from collections import Counter
n = int(input())
a = []
for i in range(n):
    a.append(input())
a.sort()
a = list(dict.fromkeys(a))
print(a)