h, w = map(int, input().split())
s = []
lin = []
lin2 = []
for i in range(h):
    s.append(input())
for _ in range(w+2):
    lin.append("#")
for i in range(h):
    lin2.append("#"+s[i]+"#")
print(''.join(lin))
print('\n'.join(lin2))
print(''.join(lin))

H, W = map(int, input().split())
picture = [input() for _ in range(H)]

for i in range(H + 2):
    if i == 0 or i == H + 1:
        print('#' * (W + 2))
    else:
        print('#' + picture[i - 1] + '#')