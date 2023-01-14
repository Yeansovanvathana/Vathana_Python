n, t = map(int, input().split())
arr = list(map(int, input().split()))
song = 0
time = 0
lis = []
final = 0
for i in range(len(arr) * 2):

    time += arr[song]
    lis.append(time)
    if song < n - 1:
        # print(song, n)
        song += 1
    elif song == n - 1:
        song = 0
    if time > t:
        break
ans = lis[-2]
if song > 0:
    print(song, t - ans)
else:
    print(n, t - ans)
