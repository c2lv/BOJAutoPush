def collatz_conjecture(a, b):
    s = []
    x = a
    s.append(x)
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
        s.append(x)
    x = b
    steps = 0
    while x != 1:
        if x in s:
            break        
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
        steps += 1
    result = f"{a} needs {s.index(x)} steps, {b} needs {steps} steps, they meet at {x}"
    print(result)

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    collatz_conjecture(a, b)