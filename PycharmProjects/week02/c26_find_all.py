def find_all(lis, value):
    list1 = []
    for i in range(len(lis)):
        if lis[i] == value:
            list1.append(i)
    if len(list1) == 0:
        return None
    return list1
find_all([1,5,12,5,4],5)

# find first
def find_first(list, value):
    position = list.index(value)
    return position
find_first(['100','100','200','300'],'100')