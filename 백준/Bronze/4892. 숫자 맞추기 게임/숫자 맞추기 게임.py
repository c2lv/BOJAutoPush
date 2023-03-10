i = 1
while True:
    n = int(input())
    if n != 0:
        if n % 2 == 1:
            print(f"{i}. odd {(n - 1) // 2}")
        else:
            print(f"{i}. even {n // 2}")
        i += 1
    else:
         break   