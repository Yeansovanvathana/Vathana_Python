def list_to_lists(lis):
    lis1 = []
    for i in lis:
        lis2 = []
        for x in i:
            lis2.append(x)
        lis1.append(lis2[::-1])
    return lis1
print(list_to_lists(["Hello","World"]))