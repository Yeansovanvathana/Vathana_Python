n, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
arr = []
for i in range(n):
    arr.append(i+1)
I1 = arr[-1]
I2 = arr[-2]
arr.pop(-1)
arr.pop(-1)
arr.append(I1)
arr.append(I2)

print(*arr)