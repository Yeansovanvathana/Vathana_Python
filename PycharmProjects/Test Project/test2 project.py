import time
name = input("what is your name? ")
print(f"Hello, {name} Time to play hangman!")
print("")
time.sleep(1)
print()
"Start guessing..."
time.sleep(0.5)
Word = "communicate"
guesses = ""
turns = 10
failed = 0
while turns >0:
    for chart in Word:
        if chart in guesses:
            print(chart)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win")
    break
print()
guess = input("guess a character:")
guesses += guess
if guess not in Word:
    turns -= 1
    print("Wrong")
print(f"You have {turns} more guess")
if turns == 0:
    print("You Loose")


