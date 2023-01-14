N, A, B = map(int, input().split())
ans = 0
a = N // (A + B)
b = N % (A + B)
c = min(b, A)

print(a * A + c)

N, A, B = map(int, input().split())
AB = A + B
ans = N // AB * A
C = N % AB
if C <= A:
    ans += C
else:
    ans += A
print(ans)