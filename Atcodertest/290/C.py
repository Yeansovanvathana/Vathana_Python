import random

def max_mex(A, K):
    max_mex_value = -1

    for i in range(len(A) - K + 1):
        B = random.sample(A[i:i+K], K)
        T = set(B)
        mex_value = None

        for j in range(len(A) + 1):
            if j not in T:
                mex_value = j
                break

        if mex_value is not None and mex_value > max_mex_value:
            max_mex_value = mex_value

    return max_mex_value


N, K = map(int, input().split())
A = list(map(int, input().split()))

print(max_mex(A, K))
