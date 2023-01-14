N, K = map(int, input().split())
if(K % 2 != 0):
    x = N // K
    print(pow(x, 3))

else:
    x = N // K
    y = (N + (K // 2)) // K
    print(pow(x, 3) + pow(y, 3))
