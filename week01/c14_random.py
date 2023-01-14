import random
num = int(input("Enter a number: "))

if num <= 0:
    print("ERROR")
else:
    for num1 in random.randint(1, num+1):
        if num == num1:
            print(num1, end="")
        else:
            print(num1, end=",")