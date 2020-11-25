user_input = input("Enter something: ")
if user_input == "":
    print("EMPTY")
else:
    n = 1
    user_input = user_input.replace(" ", "")
    for i in user_input:
        i = user_input.capitalize()
        i=n*i
        print(i, end="-")
        n = n + 1
    print(i)
