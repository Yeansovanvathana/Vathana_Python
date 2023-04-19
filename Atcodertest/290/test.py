T = int(input())

# Precompute marked squares for each possible value of K
marked_squares = []
for K in range(1, 10001):
    squares = [0]
    for i in range(1, 10001):
        next_square = (squares[-1] + i) % K
        while next_square in squares:
            next_square = (next_square + 1) % K
        squares.append(next_square)
    marked_squares.append(squares)

# Process test cases
for i in range(T):
    N, D, K = map(int, input().split())
    print(marked_squares[K - 1][N - 1])
