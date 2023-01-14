N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, None)
arr2 = []
for _ in range(N+1):
    arr2.append(None)
ans = 1
for i in range(1, K + 1):
    # print(i, arr2[ans], arr[ans])
    if arr2[ans] == None:
        arr2[ans] = i
        ans = arr[ans]
    else:
        for _ in range((K - i + 1) % (i - arr2[ans])):
            ans = arr[ans]
        break

print(ans)
