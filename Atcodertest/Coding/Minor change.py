S = input()
T = input()
W = 0
for i in range(len(S)):
    if S[i] != T[i]:
        W += 1
print(W)