n = int(input())
A = list(map(int, input().split()))

ans = []

for idx, a in enumerate(A):
    ans.append((a, idx + 1))
print(ans)
ans.sort()
print(ans)

for number, idx in ans:
    print(idx, end=" ")