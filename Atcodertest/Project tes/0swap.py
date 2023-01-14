n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n):
    if p[i] == i+1:
        print(p[i])
        ans += 1
print(ans)
if ans >= n-2:
    print("YES")
else: print("NO")
