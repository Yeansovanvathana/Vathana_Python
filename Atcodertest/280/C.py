s = input()
t = input()
ans = 0
for i, char in enumerate(s):
    ans += 1
    if t[i] != char:
        print(ans)
        exit()
print(len(t))