a=input("enter a word:")
if len(a)==2:
    print( a * 2 )
elif len(a)==1:
    print(a*4)
elif len(a)==0:
    print('a'*4)
else:
    print(a[0]+a[1]+a[-2]+a[-1])