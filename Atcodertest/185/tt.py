N, M, T = map(int, input().split())
time_coffee = []
for i in range(M):
    time_coffee.append(input().split())
d = N
c = 0
for i in time_coffee:
    a = int(i[0]) - c
    d = d - a
    if d <= 0:
        print("No")
        quit()
    b = int(i[1]) - int(i[0])
    d = d + b
    if d > N:
        d = N
    c = int(i[1])
else:
    if d > T - c:
        print("Yes")
    else:
        print("No")