a='google'
dict={}
for i in a:
    key = dict.keys()
    if i in key:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)