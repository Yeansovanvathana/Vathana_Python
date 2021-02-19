H, W = map(int, input().split())
block_stack = 0
lis = []
for x in range(H):
    lis += [int(i) for i in input().split()]
lis.sort()
for i in lis:
    if i > lis[0]:
        block_stack += i - lis[0]
print(block_stack)

