n = int(input())
arr = [int(n) for n in input().split()]
j = 0
y = []
for i in arr:
    y.append(i)
first_num = y[0]
y.sort()
for word in y:
    if y[word] == word:
        j += 1
print(j)


