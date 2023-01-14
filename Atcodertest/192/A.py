# x = int(input())
# for i in range(1, 101):
#     if (x + i) % 100 == 0:
#         print(i)
def eCount(s):
    count = 0
    s = s.lower()
    for i in s:
        if i == 'e':
            count+=1
    return count
s = "helloEeeeeE"
print(eCount(s))

