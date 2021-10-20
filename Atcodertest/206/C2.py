def cntgloves(arr, n):
    count = 0
    print(arr)
    i = 0
    ans = 0
    while i < (n - 1):
        print(arr[i], arr[i+1])
        if (arr[i] == arr[i + 1]):
            count += 1
            i = i + 2
        else:
            i += 1
            ans += 1
    return ans

n = int(input())
arr = list(map(int, input().split()))
print(cntgloves(arr, n))

