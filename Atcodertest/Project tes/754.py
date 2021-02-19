s = input()
x = 753
for i in range(0, len(s) -2):
    n = int(s[i:i+3])
    x = min(x, abs(753 - n))
print(x)
