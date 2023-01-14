import time
num = int(input("Enter your the time to boom :.."))
time.sleep(1)
i = 0
while i < num:
    print(num)
    time.sleep(2)
    num -= 1
time.sleep(3)
print("Boom!")

