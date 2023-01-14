a = int(input())
b = int(input())
c = int(input())
pos1 = a + (b * c)
pos2 = a * (b + c)
pos3 = a * b * c
pos4 = (a + b) * c
pos5 = a + b + c
arr = [pos1, pos2, pos3, pos4, pos5]
print(max(arr))
