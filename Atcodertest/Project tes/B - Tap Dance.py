s = input()
for i in range(len(s)):
    if (i+1) % 2 == 0:
        if s[i] == 'R':
            print("No")

            exit()
    else:
        if s[i] == 'L':
            print("No")
            exit()
print("Yes")