n = int(input())
a = list(map(int, input().split()))

called = set()
for i in range(n):
    if a[i] not in called:
        called.add(a[i])
    elif a[i]+1 not in called and a[i]+1 <= n:
        called.add(a[i]+1)

remaining = sorted(set(range(1, n+1)) - called)

print(len(remaining))
if remaining:
    print(*remaining)
