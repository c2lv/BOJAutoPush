pixels = []
for i in range(15):
    pixels = list(input().split())
    for pixel in pixels:
        if pixel == 'w':
            cat = 'chunbae'
        elif pixel == 'b':
            cat = 'nabi'
        elif pixel == 'g':
            cat = 'yeongcheol'
print(cat)