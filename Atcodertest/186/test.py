def Unlucky(N):
    ans = 0
    i = 1
    while i <= N:
        dec = map(int, str(i))
        octal = oct(i)
        if '7' not in octal and 7 not in dec:
            ans += 1
        i += 1
    return ans
N = int(input())
print(Unlucky(N))
