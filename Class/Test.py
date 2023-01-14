s = input()
a, b = map(int, input().split())
a1 = s[a - 1]
b1 = s[b - 1]
print(a1, b1)
s1 = s.replace(a1, b1)
ans = s1.replace(b1, 's')
# s = s1.replace(b1, a1)
print(s)
print(s1)
print(ans)