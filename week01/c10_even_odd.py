try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Bad input.")

else:
    if user_input % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
