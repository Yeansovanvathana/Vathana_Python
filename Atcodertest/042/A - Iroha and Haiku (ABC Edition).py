ABC = list(map(int, input().split()))
if ABC.count(5) == 2 and ABC.count(7) == 1:
    print("YES")
else:
    print("NO")
# ABC = list(map(int, input().split()))
# print("YES" if ABC.count(5) == 2 and ABC.count(7) == 1 else "NO")