N, M = map(int, input().split())
ans = [0 for i in range(N)]
pen = [0 for i in range(N)]
# print(ans, pen)
for i in range(M):
    p, S = input().split()
    p = int(p) - 1
    if ans[p] == 0:
        if S == "AC":
            ans[p] = 1
            # print('ans')
            # print(ans)
        else:
            pen[p] += 1
            # print('pen')
            # print(pen)
# print(ans, pen)

ANS = sum(ans)
PEN = 0
for i in range(N):
    # ANS += ans[i]
    PEN += ans[i] * pen[i]

print(ANS, PEN)