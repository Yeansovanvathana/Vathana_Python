N = int(input())
P = [0, 0] + list(map(int, input().split()))
print(P)
curr = N
cnt = 0

while curr != 1:
    cnt += 1
    curr = P[curr]
    print(P[curr])
print(cnt)