N, X, T = map(int, input().split())
Z = (N + X - 1) // X * T
print(Z)
៊#2
N, X, T = map(int,input().split())
if N % X == 0:
    print(N//X*T)
else:
    print(N//X*T+T)