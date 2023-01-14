n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    ans += 1
    if i == k:
        break
print(ans)