# a, b = map(int, input().split())
n = input()
a = int(n[1]+n[-1]+n[0])
b = int(n[-1]+n[0]+n[1])
n = int(n)
print(n+a+b)