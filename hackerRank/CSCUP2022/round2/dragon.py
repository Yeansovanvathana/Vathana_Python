s, n = map(int, input().split())

drangon = []
bonus = []

for i in range(n):
    x, y = map(int, input().split())
    drangon.append(x)
    bonus.append(y)
bob = s
# print(bonus, drangon)
for j in range(n):
    # print(bob)
    # print(bob, drangon[j])
    if bob >= drangon[j]:
        bob += bonus[j]
        # print(bob, drangon[i])
    else:
        print("NO")
        exit()

print("YES")