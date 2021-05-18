n = int(input())
lis =[]
ans1 = 0
for i in range(n):
    lis.append(list(map(int, input().split())))
for i in range(n):
    if lis[i][0] == lis[i][1]:
        ans1 += 1
    else: ans1 = 0
    if ans1 == 3:
        print("Yes")
        exit()
print("No")


