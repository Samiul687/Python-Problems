def pig_it(text):
    text = text.split()
    complete = []

    for word in text:

        if word.isalpha():
            first = word[1:]
            second = word[0] + "ay"

            complete.append(first + second)
        else:
            complete.append(word)

    complete = " ".join(complete)

    return complete
