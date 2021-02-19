N = int(input())
ans = 1
for i in range(1, N+1):
    ans = (ans * i) % 1000000007
print(ans)

# import math
# print(math.factorial(int(input()))%(10**9+7))

# N = int(input())
#     ans = 1
#     for i in range(1, N + 1):
#         ans *= i
#         ans %= 10 ** 9 + 7
#     print(ans % (10 ** 9 + 7))