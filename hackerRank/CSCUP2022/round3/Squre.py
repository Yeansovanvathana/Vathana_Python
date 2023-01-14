x1, y1, x2, y2 = map(int, input().split())
directionX = x2 - x1
directionY = y2 - y1
x3 = x2 - directionY
y3 = y2 + directionX
x4 = x1 - directionY
y4 = y1 + directionX
print(x3, y3, x4, y4)