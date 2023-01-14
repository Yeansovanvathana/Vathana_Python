import math
k, n = map(int, input().split())
c = n/k
c = math.floor(c)
ans = k * c
final = n - ans

print(c+1, final)
