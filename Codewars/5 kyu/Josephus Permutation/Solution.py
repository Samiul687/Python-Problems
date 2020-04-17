def josephus(items, k):
    index = -1
    counter = 1
    ignore = []
    solution = []

    while len(ignore) < len(items):
        index = 0
        for char in items:
            if index in ignore:
                index += 1
            else:
                if counter % k == 0:
                    ignore.append(index)
                index += 1
                counter += 1
    for num in ignore:
        solution.append(items[num])

    return solution
