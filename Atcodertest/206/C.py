def pair(arr):
    count = 0
    index = 1
    ans = 0
    for i in arr:
        for j in arr[index:]:
            if i != j:
                ans += 1
        index += 1
    return ans

n = int(input())
arr = list(map(int, input().split()))
print(pair(arr))
