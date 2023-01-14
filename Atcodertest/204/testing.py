n, m = map(int, input().split())
lis = []
b = []
if m > 0:
    for i in range(n):
        lis.append(list(map(int, input().split())))
        b.append(lis[i][1])
    lis.sort()
    ans = []
    for i in range(n):
        for j in range(n):
            if lis[i][0] != b[j]:
                ans.append([lis[i][0], b[j]])
    ans = set(tuple(row) for row in ans)
    print(len(ans) + n)
else: print(n)