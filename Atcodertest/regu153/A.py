# def nth_beautiful(n):
#     return int(str(n) + '1' + '0'*7)
# n = int(input())
# print(nth_beautiful(n))
n = input()
ans = []
for i in n:
    if i == "0":
        ans.append('1')
    else:
        ans.append('0')
print(''.join(ans))