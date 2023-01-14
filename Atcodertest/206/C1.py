from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))
res = list(combinations(arr, 2))

print(res)
# for i in res:
#     if i[0] == i[1]:
#         res.remove(i)
# print(len(res))