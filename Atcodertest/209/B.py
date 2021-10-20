n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in range(len(arr)):
    if (i+1) % 2 == 0:
        ans.append(arr[i] - 1)
    else:
        ans.append(arr[i])
# print(ans)
if sum(ans) <= x:
    print("Yes")
else:
    print("No")