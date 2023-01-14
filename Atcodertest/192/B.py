s = str(input())
count = 0
lis = []
for i in s:
    lis.append(i.isupper())
for j in lis:
    if lis[j] == False:
        count += 1
    else:
        count -= 1
if lis[0] != False:
    print("No")
elif lis[-1] == True:
    if count != 0:
        print("No")
    else:
        print("Yes")
elif lis[-1] == False:
    if count > 0:
        print("Yes")
else:
    print("Yes")











