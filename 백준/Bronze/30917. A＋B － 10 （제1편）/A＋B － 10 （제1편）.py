for i in range(1, 10):
    print("?", "A", i, flush=True)
    n = int(input())
    if n == 1:
        a = i
        break
for i in range(1, 10):
    print("?", "B", i, flush=True)
    n = int(input())
    if n == 1:
        b = i
        break
print("!", a + b)