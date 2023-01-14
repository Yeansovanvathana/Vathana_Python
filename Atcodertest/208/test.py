P = int(input())
factorial = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]
def func(numb):
    for i in range(len(factorial)):
        if factorial[i] > numb:
            break
    return i-1
count = 0
while P > 0:
    index = func(P)
    P -= factorial[index]
    count += 1
print(count)