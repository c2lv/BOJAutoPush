def solve(p, k):
    for i in range(2, k):
        if p % i == 0:
            print("BAD", i)
            return
    print("GOOD")
    return

p, k = map(int, input().split())
solve(p, k)