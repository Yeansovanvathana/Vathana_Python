
MOD = 998_244_353
def main(A, B, C):
    def f(x):
        return x * (x + 1) // 2

    return f(A) * f(B) * f(C) % MOD


a, b, c = map(int, input().split())
print(main(a, b, c))