a, b = map(int, input().split())
ans = 0
for i in range(a):
    n = input()
    f = n.count('#')
    ans += f
print(ans)