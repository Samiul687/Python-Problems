def dig_pow(n, p):
    numbers = []
    i = 0
    powers = []
    total = 0
    string = str(n)

    for char in string:
        numbers.append(int(char))

    for x in range(p, p + len(string)):
        powers.append(numbers[i] ** x)
        i += 1

    for p in powers:
        total += p

    if total % n == 0:
        return int(total/n)
    else:
        return -1
