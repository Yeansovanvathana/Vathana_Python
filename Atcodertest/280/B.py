
n = int(input())
arr = list(map(int, input().split()))
ans = 1
output = []
output.append(arr[0]);
prefix = arr[0]
while (ans < len(arr)):
    prefix = arr[ans] - sum(output)
    output.append(prefix)
    ans = ans + 1
print(*output)