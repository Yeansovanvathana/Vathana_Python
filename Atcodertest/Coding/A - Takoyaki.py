N, X, T = map(int, input().split())
P = 1
if X > 1:
    while True:
        value = int(N / X)
        re = N % X
        if re == 0:
            P = value
            Time = T * P
            break
        else:
            P += value
            Time = T * P
            break
else:
    Time = T * N
print(Time)