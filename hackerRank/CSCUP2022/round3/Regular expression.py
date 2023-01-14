def MatchString(s, p):

    if p[-1] != '*':
        if s and (p[-1] == s[-1] or p[-1] == '.'):
            return MatchString(s[:-1], p[:-1])
        else:
            return False
    else:
        new = p[-2]
        if s and (s[-1] == new or new == '.'):
            return MatchString(s[:-1], p)
        else:
            return MatchString(s, p[:-2])

s = input()
p = input()
result = MatchString(s, p)
print(0) if result == True else print(1)