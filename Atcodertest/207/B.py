a, b, c, d = map(int, input().split())
ans = a
final = 0
for i in range(a):
    ans += b
    final += c
    end = final * d
    if ans <= end:
        print(i+1)
        exit()
print('-1')