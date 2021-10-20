from collections import Counter, defaultdict
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
Count_A = Counter(A)
index_B = defaultdict(int)
Count_C = Counter(C)
for index, res in enumerate(B, 1):
    if res in index_B:
        index_B[res].append(index)
    else:
        index_B[res] = [index]
result = 0
for key,value in Count_A.items():
    if key in index_B:
        for val in index_B[key]:
            if val in Count_C:
                result += value * Count_C[val]
print(result)