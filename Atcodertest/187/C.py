N = int(input())
x = []
z = []
I = []
for i in range(N):
    x.append(input())
for j in x:
    if j[0] == '!':
        replace = j.replace('!', '')
        z.append(replace)
for p in x:
    for q in z:
        if p == q:
            I.append(p)
if I:
    print(I[0])
else:
    print("satisfiable")







