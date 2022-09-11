s = input()
happy = s.count(":-)")
sad = s.count(":-(")
if happy == sad:
    if happy > 0:
        print('unsure')
    else:
        print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')