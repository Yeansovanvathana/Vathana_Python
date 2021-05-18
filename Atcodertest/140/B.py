n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
res = 0
for i in a:
    res += b[i - 1]
    print(i,"i")
    print(b[i-1])
# for i, j in zip(a, a[1:]):
#     if j == i + 1:
#         res += c[i - 1]
print(res)