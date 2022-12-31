t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    for _ in range(n):
        school_name, drink = input().split()
        d[school_name] = int(drink)
    d = sorted(d.items(), key=lambda x:x[1], reverse=True)
    print(d[0][0])