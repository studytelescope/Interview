
def HTMLElements(strParam):

    tags = {
        'div': 0,
        'b': 0,
        'i': 0,
        'p': 0,
        'em': 0,
    }

    terms = strParam.replace('>', '<').split('<')

    for item in terms:
        if item == '':
            terms.remove(item)

    for key in tags:
        for item in terms:
            if key == item or '/' + key == item:
                tags[key] += 1

    for key in tags:
        if tags[key] % 2 == 0:
            for unit in terms:
                if unit == key or unit == '/' + key:
                    terms.remove(unit)

    for item in terms:
        if item[0] != '/':
            for i in range(terms.index(item) + 1, len(terms)):
                # if terms[i] == '/' and terms[i] == '/' + item:
                if terms[i] == '/' and terms[i] != '/' + item:
                    print('position = ', terms.index(item), ", tag = ", item)

    print(terms)
    print(tags)

    return strParam

# keep this function call here
print(HTMLElements("<div></div><i></i><p><i></div><i></i></p>"))