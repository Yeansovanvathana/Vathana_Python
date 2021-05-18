a = list(map(int, input().split()))
count = []
for i in a:
    if i in count:
        count.append(i)
    else:
        print(i)
print(count)