s = input()
a = []
for i in s:
    if i == '0':
        a.append('0')
    elif i == '1':
        a.append('1')
    elif i == '6':
        a.append('9')
    elif i == '8':
        a.append('8')
    elif i == '9':
        a.append('6')
ans = ''.join(a)
print(ans[::-1])