def no_odds(values):
    even = []

    for v in values:
        if v % 2 == 0:
            even.append(v)
    return even
