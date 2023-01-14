import itertools
from itertools import product

N, X = map(int, input().split())

xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]


c = list(itertools.product(x, y))
arr = []
for i in c:
   arr.append(sum(i))
if X in arr:
    print("Yes")
else:
    print("No")