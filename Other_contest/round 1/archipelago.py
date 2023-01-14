n, m = map(int, input().split())
set_a = set()
set_b = set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1: set_a.add(b)
    if b == n: set_b.add(a)
if set_b & set_a:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     ans += arr[i]
#     print("II")
#     print(arr[i])
#     print("ans")
#     print(ans)
#     if ans + arr[-1] == n:
#         print("Yes")
#         exit()
#
# print(ans)