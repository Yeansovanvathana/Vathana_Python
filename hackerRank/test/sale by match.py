from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
lis = []
ans = Counter(arr)
print(ans)
s = 0
for i in ans:
    s += ans[i]//2
print(s)
