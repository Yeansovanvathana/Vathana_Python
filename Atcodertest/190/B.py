n, s, d = map(int, input().split())
lis = []
a = 0
for i in range(n):
    lis.append(list(map(int, input().split())))
for i in range(n):
    if lis[i][0] < s and lis[i][1] > d:
        a += 1
        break
print("Yes") if a> 0 else print("No")