n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    if i >= k:
        ans += 1
print(ans)