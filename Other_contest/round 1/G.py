n = int(input())
arr = list(map(int, input().split()))
k = int(input())
ans = k
s = 0
for i in range(10):
    print(ans)
    for x in range(10):
        if arr[x] == arr[ans - 1]:
            s += 1
            ans += 1
            print('=')
            print(ans)
        elif ans < n:
            print('<')
            s += 1
            ans += 1
            if ans == arr[k-1]:
                exit()
        elif ans > n:
            print('>')
            s += 1
            ans = ans - n
            if ans == arr[k-1]:
                exit()

print(s)