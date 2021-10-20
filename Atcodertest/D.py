n, k = map(int, input().split())
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    print(a, b)
    for j in range(0, 5):
        k -= 1

        ans += 1
        print('ans')
        print(ans)
        print('k')
        print(k)
        print('a')
        print(a)
        if k == a:
            k += b
            k -= 1
            print('k+')
            print(k)
        elif k <= 0:
            break
print(ans)