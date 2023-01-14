h, a = map(int, input().split())
ans = h - a
x = 1
for i in range(h):
    if ans < h:
        x += 1
        if ans <= 0:
            exit()
print(x)
