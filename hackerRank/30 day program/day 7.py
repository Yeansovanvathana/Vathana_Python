n = int(input())
arr = [int(n) for n in input().split()]
print(' '.join(map(str, arr[::-1])))
