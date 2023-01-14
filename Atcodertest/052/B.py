N = int(input())
S = str(input())
max_value = 0
ans = 0
for i in range(N):
    if S[i] == 'I':
       ans += 1
    else:
        ans -= 1
    max_value = max(max_value, ans)
print(max_value)