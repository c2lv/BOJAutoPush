t = int(input())
for _ in range(t):
    n = int(input())
    print(f"Pairs for {n}:", end='')
    for i in range((n - 1) // 2):
        if i != 0:
            print(',', end='')
        print(f" {i + 1} {n - i - 1}", end='')
    print()