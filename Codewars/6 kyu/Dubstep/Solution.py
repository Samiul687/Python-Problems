def song_decoder(song):
    song = song.split("WUB")
    new = []
    print(song)
    for word in song:
        if word == "":
            pass
        else:
            new.append(word)

    word = " ".join(new)

    return word
