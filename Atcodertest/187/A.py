N = int(input())
z = []
I = []
ans = []
for i in range(N):
    x = str(input())
    I.append(x)
    if x[0] == '!':
        re = x.replace('!', '')
        z.append(re)
# for p in I:
#     for q in z:
#         if p == q:
#             ans.append(p)

if ans:
    print(ans[0])
else:
    print("satisfiable")








