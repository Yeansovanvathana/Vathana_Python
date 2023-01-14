n, w = map(int, input().split())
arr = list(map(int, input().split()))
print(sum(arr))
ans = 0
num = 0
for i in range(n):
    # print('ans')
    # print(ans)
    # print('i')
    # print(i)
    print(arr[i])
    if arr[i] < w:
        ans += 1
    num += i
if num < w:
    ans += 1
print(ans)