def fun_sort(list):
    list.sort()
    return list
print(fun_sort([1,5,12,5,4]))

# sort reverse
def fun_sort_rev(list):
    list=sorted(list, reverse=True)
    return list
fun_sort_rev(['300','100','200','400'])

