S = input()
S = S.lower()
if S[-1] != 's':
    S = S+'s'
    print(S)
elif S[-1] == 's':
    S = S + 'es'
    print(S)
else:
    print(S)