cycle1 = ['a', 'i', 'y', 'e', 'o', 'u']
cycle2 = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

while True:
    try:
        s = input()
        for c in s:
            a = c.lower()
            if a in cycle1:
                a = cycle1[(cycle1.index(a) + 3) % 6]
            elif a in cycle2:
                a = cycle2[(cycle2.index(a) + 10) % 20]
            if c.isupper():
                a = a.upper()
            print(a, end="")
        print()
    except EOFError:
        break