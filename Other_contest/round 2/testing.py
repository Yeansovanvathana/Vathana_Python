def getProduct(n):
    product = 1

    while (n != 0):
        product = product * (n % 10)
        n = n // 10

    return product


n = int(input())
print(getProduct(n))