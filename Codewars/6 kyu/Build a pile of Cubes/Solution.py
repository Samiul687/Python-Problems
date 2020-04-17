def find_nb(m):
    a = 1
    counter = 0
    total = 0

    if m == "":
        return 0
    else:
        while total < m:
            a = counter ** 3
            total += a
            counter += 1

        if total % m != 0:
            return -1
        else:
            return counter - 1
