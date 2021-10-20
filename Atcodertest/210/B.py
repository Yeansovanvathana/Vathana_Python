n = int(input())
s = input()
for i in range(n):
    if s[i] == '1':
        if (i+1) % 2 == 0:
            print("Aoki")
            exit()
        else:
            print("Takahashi")
            exit()
