n = int(input())
a, b, c = map(int, input().split())
weekDays = (c, c, a, c, b, a, c)
ans = 0
ans1 = []
for i in range(7):
    for j in range(7):
        ans += weekDays[j]
        if ans <= n:
            ans1.append(weekDays[j])
        else: ans = 0
print(ans1)

