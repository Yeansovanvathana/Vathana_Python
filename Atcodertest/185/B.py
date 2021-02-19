n, m, t = map(int, input().split())
s = []
d = n
c = 0
for i in range(m):
    s.append(input().split())
for i in s:
    a = int(i[0]) - c
    d = d - a
    if d <= 0:
        print("No")
        quit()
    b = int(i[1]) - int(i[0])
    d = d + b
    if d > n:
        d = n
    c = int(i[1])
else:
    if d > t - c:
        print("Yes")
    else:
        print("No")