k = int(input())
s = input()
ans = s[:k]
if len(s) <= k:
    print(s)
else:
    print(ans+'...')