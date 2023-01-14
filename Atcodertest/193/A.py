n = int(input())
ans = []
for i in range(n):
    t, p, x = list(map(int, input().split()))
    if t < x:
        ans.append(p)
print(min(ans)) if ans else print(-1)
