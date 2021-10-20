import itertools
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(itertools.product(arr, arr))
print(arr)
lis = []
for i in arr:
    if i[0] != i[1]:
        lis.append(i[0]*i[1])
lis = sorted(set(lis))
# print(lis)
print(lis[k-1])