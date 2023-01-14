n, q = map(int, input().split())
arr = [(i, 10 ** 9) for i in map(int, input().split())]
x = []

for i in range(q):
    x.append((int(input()), i))

arr2 = arr + x
Final = sorted(arr2, reverse=True)
ans = [0] * q

count = 0
for x, i in Final:
    if i > q:
        count += 1
    else:
        ans[i] = count
for i in ans:
    print(i)