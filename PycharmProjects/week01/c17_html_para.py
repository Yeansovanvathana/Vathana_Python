book = []
while True:
    user_input = input("Enter a sentence: ")
    if user_input == "GENERATE":
        break
    if user_input != "":
        book.append(user_input)
if book == []:
    print("Nothing to display.")
for i in book:
    print("<p>%s</p>"%i)