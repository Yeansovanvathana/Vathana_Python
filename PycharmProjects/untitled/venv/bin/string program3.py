a=input('the later:')
b=len(a)
if b<2:
  print('a', '')
else:
  print('a',a[:2]+a[-2:])