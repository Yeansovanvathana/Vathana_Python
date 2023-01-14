from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
array = Counter(arr)
for i in array:
    if (array[i] % 2) != 0:
        print(i)

