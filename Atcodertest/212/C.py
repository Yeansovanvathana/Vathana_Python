n, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in a:
    for j in b:
       ans.append(abs(i-j))
print(min(ans))
