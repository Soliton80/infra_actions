def upperlowercase(text):
    newtext = str()
    for i in range(len(text)):
        if i % 2 == 0:
            newtext += text[i].upper()
        elif i % 2 != 0:
            newtext += text[i].lower()
    return newtext


print(upperlowercase(input('введите текст >>')))
