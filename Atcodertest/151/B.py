n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = max(0, n*m - sum(arr))
print(ans)