s = input()
for i in range(1, len(s)+1):
    if i % 2 == 0:
        if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
            print('Yes')
        else:
            print("No")
