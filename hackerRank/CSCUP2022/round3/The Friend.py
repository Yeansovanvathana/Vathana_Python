N, M = map(int, input().split())
ans = 0

Fri = [set() for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    Fri[A - 1].add(B)
    Fri[B - 1].add(A)
for i in Fri:
    ans = max(ans, len(i))

print(ans + 1)