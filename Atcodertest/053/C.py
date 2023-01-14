s = input()
a = s.index('A')
z = s.rfind('Z')
print(len(s[a:z])+1)