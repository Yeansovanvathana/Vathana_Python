def my(E):
    Z = 0
    for i in range(A, B):
        for j in range(C, D):
            if i == j:
                Z = 1
                return Z
    if Z > 0:
        print("Yes")
    else:
        print("No")
E = A, B, C, D = map(int, input().split())


A, B, C, D = map(int,input().split())
if C <= B and D >= A:
    print('Yes')
else:
    print('No')
