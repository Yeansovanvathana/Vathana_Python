print("The form of the linear equation in one variable is: aX + b = c")
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
print(f"The form of the linear equation in one variable is: {a}X + {b} = {c}")

firstStep = c - b
secondStep = firstStep / a
#since (10 + x) is the actual number of x
final = secondStep - 10
print(int(final))
