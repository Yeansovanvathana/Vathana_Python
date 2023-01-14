n = int(input())
s = input()
count = 0
for i in s:
    if i == 'I':
        count += 1
    else:
        count -= 1
    count = max(0, count)
print(count)