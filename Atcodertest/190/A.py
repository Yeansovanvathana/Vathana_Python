a, b, c = map(int, input().split())
if c == 0:
    if a - b > 0:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if a >= b:
        print("Takahashi")
    else:
        print("Aoki")


