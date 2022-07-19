def ulcase(text):
    ultext = str()
    for i in range(len(text)):
        if i % 2 == 0:
            ultext += text[i].upper()
        if i % 2 != 0:
            ultext += text[i].lower()
    return ultext


print(ulcase(input('>>')))