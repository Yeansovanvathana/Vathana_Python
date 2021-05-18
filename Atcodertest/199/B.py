n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    if i != 0:
        get = set(range(a[i], b[i] + 1))
        ans = list(set(ans) & set(get))
    else:
        ans = list(range(a[i], b[i] + 1))
print(len(ans))
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(len(range(max(a), min(b)+1)))