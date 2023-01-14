n = int(input())
s, t = list(input().split())
ans = []
for i in range(n):
    ans.append(s[i]+t[i])
print("".join(ans))