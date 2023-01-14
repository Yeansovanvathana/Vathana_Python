n = int(input())
num = 1
ans = []
wrong = []
# for i in range(1, n+1):
#     if pow(i, num) == n:
#         ans.append(i)
#     else:
#         wrong.append(i)
# print((wrong))
for i in range(1, n+1):
    if i**num == n:
        ans.append(i**num)
print(ans)
