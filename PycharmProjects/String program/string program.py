def dict_count(list1):
    list2= {}
    for i in list1:
        x = list1.count(i)
        list2.update({str(i): x, })
    return list2

print(dict_count('google.com'))
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))