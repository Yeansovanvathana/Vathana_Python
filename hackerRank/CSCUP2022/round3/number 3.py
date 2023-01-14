N = input()

ans = 0
for i in range(len(N)):
    ans += int(N[i])

if(ans % 3 == 0):
    print(0)
    exit()

if(len(N) == 1):
    print(-1)
    exit()

for i in range(len(N)):
    if(ans % 3 == int(N[i]) % 3):
        print(1)
        exit()
if(len(N) == 2):
    print(-1)
    exit()
else:
    print(2)
    exit()



