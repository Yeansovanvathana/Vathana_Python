import math
n = int(input())
log2 = math.log2(n)
log = str(log2)
x = log.find('.')
print(log[:x])


