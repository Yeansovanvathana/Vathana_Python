import collections

N = int(input())

s = [0] * N
t = [0] * N

for i in range(N):
    s[i], t[i] = map(str, input().split())

s.extend(t)
print(s)
c = collections.Counter(s)
c = c.most_common()
print(c[1][1])

if c[1][1] >= 2:
    print("No")
else:
    print("Yes")