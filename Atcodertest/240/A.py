s = input()
up = 0
lo = 0
for i in s:
    if i.isupper():
        up += 1
    else:
        lo += 1
# print(lo, up)
if up == lo:
    print("Yes")
elif up % 2 == 0 and up>0:
    print("Yes")
else:
    print("No")
