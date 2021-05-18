a, b, c = map(int, input().split())
if abs(c - b) == abs(b - a):
    print("Yes")
else:
    print("No")