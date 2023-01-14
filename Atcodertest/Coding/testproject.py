N = int(input())
j = 0
if N >= 3:
    D = [input().split() for _ in range(N)]
    for i in D:
        if i[0] == i[1]:
            j += 1
    if j == 3:
        print("Yes")
    elif j == 6:
        print("Yes")
    elif j != 3:
        print("No")
    else:
        print("No")

