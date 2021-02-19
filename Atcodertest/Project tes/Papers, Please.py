n = int(input())
a = list(map(int, input().split()))
ans = 0
even = []
for i in range(n):
    if a[i] % 2 == 0:
        even.append(i)
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            ans += 1
print("APPROVED") if (ans == len(even)) else print("DENIED")
