import math
v, a, b, c = map(int, input().split())
arr = [a, b, c]

num = math.ceil(v / sum(arr)) - 1
sum_before_end = (num * sum(arr))

if sum_before_end + a > v:
    print("F")
elif sum_before_end + a + b > v:
    (print("M"))
elif sum_before_end + a + b + c > v:
    print("T")
else:
    print("F")
