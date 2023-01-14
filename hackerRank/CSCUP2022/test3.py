l1, r1, l2, r2 = map(int, input().split())
red = l2
blue = r1
if l2 >= r1:
    print(0)
else:
    print(r1-l2)