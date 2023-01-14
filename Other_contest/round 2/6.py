# n = int(input())
# ans = [5]
# for i in range(n):
#     ans.append(ans[i] + 10)
#     if ans[n-1]:
#         print(ans[n-1]**2)
#         break
# for i in range(1, n+1):
#     if i == n:
#         print(ans**2)
#     ans += 10

n = int(input())
if n == 1:
    print(5**2)
else:
    ans = ((n-1) * 10) + 5
    print(ans**2)


