x = input()
for i in range(len(x)):
    if i % 2 != 0:
        if x[i].islower():
            print('No')
            exit()
    else:
        if x[i].isupper():
            print('No')
            exit()
print('Yes')