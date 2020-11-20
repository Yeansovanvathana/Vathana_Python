n = input()
l = len(n)
s = [0] * 3
for i in n:
    s[int(i) % 3] += 1
s_sum = s[1] + s[2] * 2

if s_sum % 3 == 0:
    print(0)
elif s_sum % 3 == 1:
    if s[1] != 0 and l > 1:
        print(1)
    elif s[2] >= 2 and l > 2:
        print(2)
    else:
        print(-1)
else:
    if s[2] != 0 and l > 1:
        print(1)
    elif s[1] >= 2 and l > 2:
        print(2)
    else:
        print(-1)