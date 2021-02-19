X, Y = map(int, input().split())
if X > Y:
    if Y+3 > X:
        print("Yes")
    else:
        print("No")
else:
    if X+3 > Y:
        print("Yes")
    else:
        print("No")