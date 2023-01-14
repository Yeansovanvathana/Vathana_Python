def int_list(list):
    for i in list:
        if isinstance(i, int):
            return True
        return False
    return False
int_list([])
int_list([1, 2, 3])
int_list([1.5, 2, 2.0])
int_list([100, 200, 300, 400, 500])
int_list(['100', '100', '200', '300'])