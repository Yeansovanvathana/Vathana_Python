# a1, a2, a3 = map(int, input().split())
# if a1 + a2 + a3 >= 22:
#     print('bust')
# else: print('win')
a, b, c = map(int, input().split())
if a == b:
    print(c)
elif a == c:
    print(b)
elif b == a:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)
elif c == b:
    print(a)
else: print(0)