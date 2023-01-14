h, w = map(int, input().split())
s = []
t = []
for i in range(h*2):
    if (i < (h*2)/2):
        s.append(input())
    else:
        t.append(input())
ans = []
for i in range(len(s)):
    if sorted(s[i]) != sorted(t[i]):
        print("No")
        exit()
print("Yes")
# print(sorted(s[1]), sorted(t[1]))
# print()
# print(s, t)
