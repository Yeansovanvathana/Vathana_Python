n = int(input())
arr = set()
firstChar = ['H', 'D', 'C', 'S']
secondChar = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
for i in range(n):
    a = input()
    if a in arr or a[0] not in firstChar or a[1] not in secondChar:
        print("No")
        exit()
    arr.add(a)
print("Yes")