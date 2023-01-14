def list_number(start, end):
    list1 = []
    for i in range(start, end+1):
        list1.append(i)
    return list1
list_number(1,10)

#reversed
def list_number(start, end, reversed):
    list1 = []
    if reversed == True:
        for i in range(start, end+1):
            list1.append(i)
        return list1[::-1]
    else:
        for i in range(start, end + 1):
            list1.append(i)
        return list1
list_number(20, 25, reversed = True)
