import collections
n = int(input())
arr = list(map(int, input().split()))
ans = collections.Counter(arr)
print(len(ans))
