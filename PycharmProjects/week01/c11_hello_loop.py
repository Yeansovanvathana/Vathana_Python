num = input("Enter a number: ")
letter = "Hello World!"
i = 1
if len(num) != 0:
    while i <= int(num):
        if int(num) > 0:
            print(letter)
        i += 1
else:
    print("")