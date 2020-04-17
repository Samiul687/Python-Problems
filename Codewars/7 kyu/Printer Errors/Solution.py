def printer_error(s):
    allowed = "abcdefghijklm"
    counter = 0

    for char in s:
        if char not in allowed:
            counter += 1

    return str(counter)+"/"+str(len(s))
