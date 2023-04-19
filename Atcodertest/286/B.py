def solve(A, P, Q, R, S):
    left_part = A[:P-1] + A[R-1:S] + A[Q:R-1]
    right_part = A[P-1:Q] + A[S:]
    B = left_part + right_part
    return B

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

print(*solve(A, P, Q, R, S))
