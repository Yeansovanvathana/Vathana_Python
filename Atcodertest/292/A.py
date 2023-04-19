n = input()
for i in range(len(n)//2):
    n = n[:2*i] + n[2*i+1] + n[2*i] + n[2*i+2:]
print(n)