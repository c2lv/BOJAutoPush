d = {'lower': 0, 'upper': 0, 'digit': 0, 'space': 0}
while True:
    try:
        s = input()
        for key in d:
            d[key] = 0
        for c in s:
            if c.isdigit():
                d['digit'] += 1
            elif c.isspace():
                d['space'] += 1
            elif c.isupper():
                d['upper'] += 1
            else:
                d['lower'] += 1
        for key in d:
            print(d[key], end=' ')
        print()
    except:
        break