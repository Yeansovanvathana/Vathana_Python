def sort_set(lis):
    lis = sorted(set(lis))
    return lis
sort_set(['A','B','C','C','B'])

# set_sort_reverse
def sort_set_rev(lis):
    lis1 = sorted(set(lis), reverse=True)
    return lis1
sort_set_rev(['A','B','C','D','E'])
