K = int(input())
num = 0
lis = []
for i in range(K):
    num += i
    if num <= K:
        lis.append(i)
print(lis[-1])
