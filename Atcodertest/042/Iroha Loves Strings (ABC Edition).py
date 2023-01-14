N, L = map(int, input().split())
Str = []
for i in range(N):
    x = str(input())
    Str.append(x)
Str.sort()
Y = ""
for i in range(N):
    Y = Y + Str[i]
print(Y)
