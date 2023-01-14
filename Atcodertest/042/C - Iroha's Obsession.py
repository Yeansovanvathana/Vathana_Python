n, k = map(int, input().split())
d = list(input().split())
while True:
    c = 0
    for m in range(k):
        if d[m] in str(n):
            c += 1
    if c == 0:
        print(n)
        break
    else:
        n += 1