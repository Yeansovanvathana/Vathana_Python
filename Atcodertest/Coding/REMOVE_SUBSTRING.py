n = int(input())
s = input()
ans = 0
for i in range(n):
    cnt = 0
    for j in range(i+1, n):
        if s[j] != s[i]:
            cnt += 1
    ans += cnt
print(ans)