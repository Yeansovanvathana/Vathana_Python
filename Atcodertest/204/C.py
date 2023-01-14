n, m = map(int, input().split())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
lis.sort()
ans = 0
for i in lis:
    if i[0] > m:
        break
    else:
        if i[0] < i[1]:
            ans += (m - i[0] + 1)
        else:
            ans += (i[0] - i[1] + 1)
print(ans)
ans1.append(lis[i][1])