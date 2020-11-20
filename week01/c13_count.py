try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("ERROR")
else:
    if user_input < 0:
        print("ERROR")
    else:
        for num in range(1, user_input + 1):

            if user_input == num:
                print(num, end="")
            else:
                print(num, end=",")
