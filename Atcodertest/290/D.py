def find_kth_marked_square(N, D, K):
    marked_squares = [0]
    for i in range(1, N):
        next_square = (marked_squares[-1] + D) % N
        while next_square in marked_squares:
            next_square = (next_square + 1) % N
        marked_squares.append(next_square)
    return marked_squares[K-1]
T = int(input())
for i in range(T):
    N, D, K = map(int, input().split())
    kth_square = find_kth_marked_square(N, D, K)
    print(kth_square)
