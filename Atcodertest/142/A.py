n = int(input())
num = 0
for i in range(1, n+1):
    if i % 2 != 0:
        num += 1
ans = str(num / n)
print(ans + '000000000')

N = int(input())
ans = ((N+1)//2)/N
print(ans)

n = int(input())
even = n // 2
odd = n - even
print(float(odd / n))