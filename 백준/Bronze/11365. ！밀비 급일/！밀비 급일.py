while True:
    try:
        s = input()
        if s == 'END':
            break
        # solution 1
        # for i in range(len(s)):
        #     print(s[-1 - i], end='')
        # print()
        # solution 2
        s = ''.join(reversed(s))
        print(s)
    except:
        break