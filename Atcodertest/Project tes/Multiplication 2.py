n = int(input())
y = list(map(int, input().split()))
ans = 1
for i in range(n):
    if y[i] == 0:
        print(0)
        exit()
for i in range(n):
    ans *= y[i]
    if ans > 10**18:
        print(-1)
        exit()
print(ans)