n = int(input())
s = input()
dp = [0] * n
ans = [0] * (n-1)
for i in range(n-2, -1, -1):
    j = i+1+dp[i+1]
    while j < n and s[i] != s[j]:
        j += 1
    dp[i] = j - i - 1
    ans[i] = n - i - dp[i] - 1

print(*ans, sep='\n')
