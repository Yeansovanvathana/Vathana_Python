def can_pay(n, x, coins, memo):
    if x == 0:
        return True
    if n == 0:
        return False
    if memo[n][x] != -1:
        return memo[n][x]
    if coins[n-1][0] > x:
        memo[n][x] = can_pay(n-1, x, coins, memo)
    else:
        memo[n][x] = can_pay(n-1, x, coins, memo) or can_pay(n-1, x-coins[n-1][0], coins, memo)
    return memo[n][x]

if __name__ == '__main__':
    n, x = map(int, input().split())
    coins = []
    for i in range(n):
        a, b = map(int, input().split())
        coins.append([a, b])
    memo = [[-1 for _ in range(x + 1)] for _ in range(n + 1)]
    if can_pay(n, x, coins, memo):
        print("YES")
    else:
        print("NO")
