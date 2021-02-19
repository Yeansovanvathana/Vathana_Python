A, B = map(int, input().split())
res = list(map(int, str(A)))
res2 = list(map(int, str(B)))
X = sum(res)
Y = sum(res2)
if X > Y:
    print(X)
elif Y > X:
    print(Y)
else:
    print(X)
