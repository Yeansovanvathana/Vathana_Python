n = int(input())
s = []
l = list(input().split(" "))

for i in range(2, 1001):
    ans = 0
    for j in range(n):
        if int(l[j]) % i == 0:
            ans += 1
    s.append(ans)
print(s.index(max(s)) + 2)

N = int(input())
Alist = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(2, 1001):
    an = 0
    for a in Alist:
        if a % i == 0:
            an += 1
    if an > cnt:
        ans = i
        cnt = an
print(ans)
