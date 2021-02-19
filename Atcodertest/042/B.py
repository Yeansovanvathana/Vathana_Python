# N = int(input())
#
# ans = 1
# for i in range(1, N+1):
#     if 2 ** i > N:
#         ans = 2 ** (i - 1)
#         print(ans)
#         break
# print(ans)

# N = int(input())
#
# i = 1
# while(1):
#     if i*2 > N:
#         break
#     i = i*2
# print(i)

# n=int(input())
# if n >= 64:
#     print("64")
# elif n >= 32:
#     print("32")
# elif n >= 16:
#     print("16")
# elif n >= 8:
#     print("8")
# elif n >= 4:
#     print("4")
# elif n >= 2:
#     print("2")
# else:
#     print("1")

# N = int(input())
# ans = 1
# while ans <= N/2:
#     ans *= 2
# print(ans)

# A
# N = input()
# print("ABC"+N)


# C - Cat Snuke and a Voyage

# def getN():
#     return int(input())
# def getNM():
#     return map(int, input().split())
# def getList():
#     return list(map(int, input().split()))
#
# N, M = getNM()
# set_a = set()
# set_b = set()
# for _ in range(M):
#     a, b = getNM()
#     if a == 1: set_a.add(b)
#     if b == N: set_b.add(a)

# if set_a & set_b:
#     ans = "POSSIBLE"
# else:
#     ans = "IMPOSSIBLE"
# print(ans)
# print(set_a)
# print(set_b)

n, m = map(int, input().split())
set_a = set()
set_b = set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1: set_a.add(b)
    if b == n: set_b.add(a)
if set_b & set_a:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
