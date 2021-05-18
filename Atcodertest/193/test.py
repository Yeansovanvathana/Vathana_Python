import math

def isPower(n):
    if (n <= 1):
        return True
    for x in range(2, (int)(math.sqrt(n)) + 1):
        p = x
        while (p <= n):
            p = p * x
            if (p == n):
                return True
    return False

n = int(input())
ans = []
wrong = []
for i in range(2, n+1):
    if (isPower(i)):
        ans.append(i)
    else:
        wrong.append(i)
print(len(wrong)+1)