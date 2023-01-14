s1 = input()
s2 = input()
s3 = input()
lis = ['ABC', 'ARC', 'AGC', 'AHC']
if s1 and s2 and s3 in lis:
    print(lis.remove(s2))
