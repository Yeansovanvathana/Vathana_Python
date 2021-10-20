n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(n):
    for x in range(n):
        if a[x] == b[c[i]-1]:
            ans += 1
print(ans)



