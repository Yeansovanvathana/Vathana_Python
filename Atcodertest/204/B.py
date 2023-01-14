n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    if arr[i] > 10:
        ans += arr[i] - 10
print(ans)