n, x = map(str, input().split())
lis = list(map(str, input().split()))
ans = []
for i in lis:
    if i != x:
        ans.append(i)
print(' '.join(ans)) if ans else print()
print(*ans) if ans else print()


