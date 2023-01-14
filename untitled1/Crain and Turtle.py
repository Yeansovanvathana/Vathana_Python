X, Y = map(int, input().split())
if Y % 2 != 0:
    print('No')
for a in range(X + 1):
    b = X - a
    if 2 * a + 4 * b == Y:
        print('Yes')