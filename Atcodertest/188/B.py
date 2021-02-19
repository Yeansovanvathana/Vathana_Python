N = int(input())
X = []
ans = 0
X1 = list(map(int, input().split()))
Y2 = list(map(int, input().split()))
for i in range(N):
    X.append(X1[i] * Y2[i])
for u in X:
    ans += u
if ans == 0:
    print("Yes")
else:
    print("No")
