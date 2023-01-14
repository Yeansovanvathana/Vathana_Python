n = int(input())
ans = []
for i in range(10*100000):
    if n > 10:
        ans.append(10)
        n -= 10
    else:
        ans.append(n)
        break
final_ans = 0
ten = 9
for i in range(len(ans)):
    if ans[i] == 10:
        if i == 0:
            final_ans += 45
        else:
            final_ans += 55
    else:
        ten -= ans[i]
        if ten == 1:
            final_ans += 45
        elif ten == 2:
            final_ans += 36
        elif ten == 3:
            final_ans += 28
        elif ten == 4:
            final_ans += 21
        elif ten == 5:
            final_ans += 15
        elif ten == 6:
            final_ans += 10
        elif ten == 7:
            final_ans += 6
        elif ten == 8:
            final_ans += 3
        elif ten == 9:
            final_ans += 1

print((final_ans)%998244353)
