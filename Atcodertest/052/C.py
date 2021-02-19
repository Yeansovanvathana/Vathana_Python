# n = int(input())
# ans = 1
# for i in range(n):
#
#     ans = ans + i % (10 ** 9 + 7)
#
# print(ans)

# import numpy
# import math
# def r(n):
#     expo = []
#     fact = math.factorial(n)
#     for i in range(2,n+1):
#         count = 0
#         while True:
#             if fact%i!=0:
#                 break
#             # fact = fact/i
#             print(fact/i)
#             count+=1
#         expo.append(count+1)
#     return numpy.prod(expo)
# print(r(int(input())))

def factors(num):
    count = []
    fact = 2
    while True:
        if num >= fact:
            if num % fact != 0:
                fact += 1
            else:
                num /= fact
                count.append(fact)
        else:
            break
    return count
fac = {}
n=int(input())
for i in range(2,n+1):
    n = factors(i)
    for j in set(n):
        if j in fac:
            fac[j] += n.count(j)
        else:
            fac[j] = n.count(j)
fac = [fac[n]+1 for n in fac]
prod = 1
for i in fac:
    prod *= i
print(prod%(10**9+7))