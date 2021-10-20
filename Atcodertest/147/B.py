# S = input()
# N = len(S)
# n = N // 2
# print(n)
# ans = n
# for i in range(n):
#   if S[i] == S[N - i - 1]:
#     ans -= 1
# print(ans)
s = input()
t = s[::-1]
print(t)
c = 0
for x in range(len(s)):
	if s[x] != t[x]:
		c += 1
print(c//2)