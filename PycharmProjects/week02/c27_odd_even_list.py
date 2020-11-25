def odd_even_list(list):
    list1 = []
    for i in list:
        if i % 2 == 0:
            list1.append("EVEN")
        else:
            list1.append("ODD")
    return list1
odd_even_list([1, 22, 111, 444])