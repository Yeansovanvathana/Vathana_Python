n = input()
if n[0] == '0':
    if n[1] and n[7] == '0' or n[2] and n[8] == '0':
        print("Yes")
    elif n[6] or n[3] or n[5]:
        print("Yes")
    else:
        print("No")
else:
    print("No")