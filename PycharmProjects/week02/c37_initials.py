def initials(lis):
    lis1 = []
    for i in lis:
        lis1.append(i.upper()[:1])
    return lis1
# initials([])
# print(initials(['united', 'stated']))
# print(initials(['World', 'Wide', 'Web']))