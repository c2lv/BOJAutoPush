n = int(input())
for _ in range(n):
    a, b = input().split()
    b = int(b)
    if 97 <= b <= 100:
        print(a, 'A+')
    elif 90 <= b:
        print(a, 'A')
    elif 87 <= b:
        print(a, 'B+')
    elif 80 <= b:
        print(a, 'B')
    elif 77 <= b:
        print(a, 'C+')
    elif 70 <= b:
        print(a, 'C')
    elif 67 <= b:
        print(a, 'D+')
    elif 60 <= b:
        print(a, 'D')
    else:
        print(a, 'F')