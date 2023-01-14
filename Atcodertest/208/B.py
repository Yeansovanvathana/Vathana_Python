p = int(input())
num = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]
count = 0
lis = 0
for i in range(len(num)):
    if p > 0:
        if num[i] > p:
            lis = i-1
        p -= num[lis]
        count += 1
print(count)


