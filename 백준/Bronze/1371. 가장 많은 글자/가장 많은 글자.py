d = {}
while True:
    try:
        s = input()
        for c in s:
            if c.isalpha():
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
    except:
        d = dict(sorted(d.items(), key=lambda x: x[0]))
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        max = 0
        for key in d:
            if max <= d[key]:
                print(key, end='')
                max = d[key]
            else:
                break
        break