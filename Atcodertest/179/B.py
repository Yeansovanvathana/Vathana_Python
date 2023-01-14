n = int(input())
arr = []
ans = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    if arr[i][0] == arr[i][1]:
        ans += 1
    else:
        ans = 0
    if ans == 3:
        print("Yes")
        exit()
print("No")

