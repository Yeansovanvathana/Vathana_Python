N = int(input())
j = 0
if N >= 3:
    for i in range(0, N):
        D = str(input())
        D = D[0::2]
        if D[0] == D[1]:
            j += 1

    if j == 3:
        print("Yes")
    elif j == 6:
        print("Yes")
    elif j != 3:
        print("No")
    else:
        print("No")
