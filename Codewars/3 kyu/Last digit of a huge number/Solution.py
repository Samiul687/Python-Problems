def last_digit(lst):
    length = len(lst)
    if length is 0:
        return 1
    if length is 1:
        return lst[0] % 10
    num = lst[length-1]
    for i in range(length-2, 0, -1):
        x = lst[i]
        if x == 1:
            num = 1
        elif num == 0:
            num = 1
        elif x == 0:
            num = 0
        else:
            num = pow(x, num, 4) + 4
    return pow(lst[0], num, 10)
