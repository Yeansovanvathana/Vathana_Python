n, k = map(int, input().split())
ans = n
for i in range(int(k/2)):
        ans = str(ans)
        ans = ans + '200'
        ans = int(ans)
        ans = int(ans / 200)
print(ans)

