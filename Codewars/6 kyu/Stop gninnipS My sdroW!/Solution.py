def spin_words(sentence):
    lst = []
    comp = []    
    i = 0

    for word in sentence.split(" "):
        lst.append(word)

    for word in lst:
        comp = []
        i += 1
        if len(word) >= 5:
            for char in word[::-1]:
                comp.append(char)
            sol = "".join(comp)
            sentence = sentence.replace(word, sol)
    return sentence
