n, m, k, c = map(int, input().split())
m = n // m
m = m * k
for i in range(int(m/c)):
    n += 1
print(n)