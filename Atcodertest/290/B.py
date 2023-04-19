n, k = map(int, input().split())
s = input()
ans = 0
final = ''
for i in s:
    if ans != k:
        if i == "o":
            ans += 1
            final += "o"
        else:
            final += "x"
    else:
        final += "x"
print(final)