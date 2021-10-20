from collections import Counter
n = int(input())
lis = []
for i in range(n):
    lis.append(input())
lis = Counter(lis)
print(len(lis))