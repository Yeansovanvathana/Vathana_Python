from heapq import merge
N = input()
K = input()
N = [int(d) for d in str(N)]
K = [int(d) for d in str(K)]
ans = list(merge(N, K))
ans = [str(x) for x in ans]

print("".join(ans))