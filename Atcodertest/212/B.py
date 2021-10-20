s = input()
s1 = int(s[0])
s2 = int(s[1])
s3 = int(s[2])
s4 = int(s[3])
ans = [s1, s2, s3, s4]
lis = 0
for i in range(len(ans)):
    lis += ans[i] + 1
    if lis <= ans[i]:
        print("Strong")
    else:
        print("Weak")
# if s1 == s2 == s3 == s4:
#     print("Weak")
# elif ans == lis:
#     print("Weak")
# elif s1 > s2 or s2 > s3 or s3 > s4:
#     print("Weak")
# else:
#     print("Strong")
print(lis)