def find_next_square(sq):
    sqrt = sq ** 0.5

    if sqrt % 1 != 0:
        return -1
    else:
        nxt = sqrt + 1
        return int(nxt**2)
