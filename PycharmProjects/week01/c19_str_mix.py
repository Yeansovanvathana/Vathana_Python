user_input = input("Enter a word: ")
if user_input == "":
    print("0000")
elif len(user_input) == 2:
    print(user_input*2)
elif len(user_input) == 1:
    print(user_input*4)
elif len(user_input) == 0:
    print(user_input*4)
elif len(user_input) > 2:
    print(user_input[:2][::-1]+user_input[len(user_input)-2::][::-1])
