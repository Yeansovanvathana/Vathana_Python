# s = input()
# t = input()
# for i in range(len(t)):
#     try:
#         if s != t:
#             print(t[-1])
#     except:
#         print("An exception occurred")
#
#
# else: print(s)
from collections import Counter
s = input()
t = input()
s1 = Counter(s)
s2 = Counter(t)
print(s1)
t = s2 - s1
print(t)
el = t.elements()
for i in el:
    print(el)
