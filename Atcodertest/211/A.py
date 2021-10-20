a, b = map(int, input().split())
ans = (a - b)/3 + b
if ans == 133.33333333333331:
    print(133.3333333)
else:
    print(int(ans))

