def disemvowel(string):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "U", "u"]
    new = []
    lofs = list(string)

    for x in range(len(lofs)):
        if lofs[x] not in vowels:
            new.append(lofs[x])
        else:
            pass

    new = "".join(new)
    return new
