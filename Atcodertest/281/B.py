# s = input()
# l1 = s[0]
# l2 = s[-1]
# l3 = s[1:-1]
# l1 = l1.isupper()
# l2 = l2.isupper()
# print(l1, l2, l3)
#
# if s[0].isupper() == False or s[-1].isupper() == False or len(s[1:-1]) != 6 or int(s[1:-1]) < 100000 or int(s[1:-1]) > 999999:
#     print("No")
#
# else:
#     print("Yes")
# if len(l3) != 6:
#     print("No")
# elif l1 == False or l2 == False:
#     print("No")
# elif int(l3) < 100000 or int(l3) > 999999:
#     print("No")
# else:
#     print("Yes")
s = input()

if s[0].isupper() == False:
    # print(1)
    print("No")
elif s[-1].isupper() == False:
    # print(2)
    print("No")
elif len(s) != 8:
    # print(3)
    print("No")
elif s[1] == '0':
    # print(4)
    print("No")
elif not s[1:-1].isdecimal():
    print("No")
else:
    print("Yes")