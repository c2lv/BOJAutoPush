def triangle(a, b, c):
    hypotenuse = max(a, b, c)
    if hypotenuse < sum([a, b, c]) - hypotenuse:
        return 1
    return 0

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif not triangle(a, b, c):
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    else:
        print('Scalene')