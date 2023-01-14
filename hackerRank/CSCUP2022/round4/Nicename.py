N = int(input())
arr = []
for i in range(N):
    a, b = map(str, input().split())
    arr.append(a)
    arr.append(b)
unique = set(arr)
if len(arr) < len(unique) + 2:
    print("Yes")
else:
    print("No")