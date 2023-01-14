from itertools import permutations

n, w = map(int, input().split())
x = list(map(int, input().split()))

perm1 = permutations(x, 1)
perm2 = permutations(x, 2)
perm3 = permutations(x, 3)

lst = []
for i in list(perm1):
    lst.append(sum(list(i)))
for i in list(perm2):
    lst.append(sum(list(i)))
for i in list(perm3):
    lst.append(sum(list(i)))

print(len([x for x in set(lst) if x < w]))