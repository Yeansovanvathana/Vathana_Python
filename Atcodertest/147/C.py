n, k = map(int, input().split())
ans = 0
lis = []
for i in range(n):
    for j in range(k):
        lis.append(str(i+1)+'0'+str(j+1))
for i in range(0, len(lis)):
    lis[i] = int(lis[i])
print(sum(lis))