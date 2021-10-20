from itertools import product
n = int(input())
arr1 = list(map(int, input().split()))
def find_missing(lst):
    return sorted(set(range(lst[0], lst[-1])) - set(lst))
arr2 = find_missing(arr1)
ans = arr1 + arr2
print(sorted(ans))