x =[int(i) for i in input().split(' ')]
y = []
for i in range(x[0]):
    y += [int(i) for i in input().split( )]
y.sort()
z = 0
for i in y:
    if i > y[0]:
        z += i - y[0]
print(z)