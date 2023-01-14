n = int(input())
arr = list(map(int, input().split()))

if n != 3:
    ans = []
    for i in range(n):
        ans.append(sum(arr[i:i + 3]))
        if i + 1 == n:
            ans.append(arr[i] + arr[0] + arr[1])

    print(max(ans))
else:
    print(sum(arr))

