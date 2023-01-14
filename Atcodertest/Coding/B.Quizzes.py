N, X = map(int, input().split())
S = str(input())

for i in S:
    if i == '0':
        X += 1
    else:
        if X:
            X -= 1
print(X)

