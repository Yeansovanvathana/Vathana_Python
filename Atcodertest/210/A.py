n, a, x, y = map(int, input().split())
ans = x * a
if a < n:
    print((y * (n - a)) + ans)
else:
    print(ans)
