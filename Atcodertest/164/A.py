a, b, c, d = map(int, input().split())
if a - b < 0:
    print('Yes')
    print("hi")
elif a - b > 0:
    if c - d < 0:
        print("Yes")
    else:
        print("No")
