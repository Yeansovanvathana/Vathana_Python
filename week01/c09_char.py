user_input = input("Enter something: ")
if user_input:
    print(f"[{user_input[0]}][{user_input[-1]}]")
else:
    print("[][]")