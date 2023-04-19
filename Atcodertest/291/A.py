n = input()
ans = 0
for i in n:
    if i.islower():
       ans += 1
    else:
        break
print(ans + 1)