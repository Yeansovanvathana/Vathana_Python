n, x = map(int, input().split())
v = []
p = []
ans = 0
for i in range(n):
        u, y = map(int, input().split())
        v.append(u)
        p.append(y)
for j in range(n):
    ans += v[j] * p[j]
    if ans/100 > x:
        print(ans+1)
        exit()
print(-1)

n, b = map(int, input().split())
v = []
a = 0
for i in range(n):
    v.append(list(map(int, input().split())))
for i in range(n):
    a += v[i][0] * v[i][1]
    if a / 100 > b:
        print(i + 1)
        exit()
print(-1)