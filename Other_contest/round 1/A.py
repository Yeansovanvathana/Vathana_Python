# def arrayAddition(arr1, N):
N = int(input())
arr = list(map(int, input().strip().split()))
print(arr)
arr1 = arr.copy()
arr1.pop(0)
arr1.pop(-1)
sets = [[]]
print(sets)
for num in arr1:
    nextPart = []
    for i in sets:
        print(i)
        nextNum = [arr[0]] + i + [num] + [arr[-1]]
        print(nextNum)
        nextPart.append(nextNum)
        # if sum(nextNum) == N:
        #     print(nextNum)
    sets += nextPart
print('No')


# print(arr1)
#
# print(arr1)




# print(arrayAddition(arr1, N))
