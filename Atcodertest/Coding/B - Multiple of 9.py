N = int(input())
x = N //1000
x1 = (N - x*1000)//100
x2 = (N - x*1000 - x1*100)//10
x3 = N - x*1000 - x1*100 - x2*10
sum = x+x1+x2+x3
if sum % 9 != 0:
    print("No")
else:
    print("Yes")