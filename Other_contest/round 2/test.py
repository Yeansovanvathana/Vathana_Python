n, k = map(int, input().split())
arr = list(map(int, input().split()))
lis = []
for a in arr:
    for b in arr:
        if a != b:
            if a * b not in arr:
                lis.append(a*b)
lis = sorted(set(lis))
print(lis[k-1])