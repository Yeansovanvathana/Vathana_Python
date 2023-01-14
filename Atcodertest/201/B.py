n = int(input())
ans = []
ans1 = []
for i in range(n):
    ans1.append(list(map(str, input().split())))
for i in ans1:
    ans.append(int(i[1]))
ans = sorted(ans)
ans = ans[::-1]
l = ans[1]
for i in ans1:
    if int(i[1]) == l:
        print(i[0])

