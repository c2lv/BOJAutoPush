import random

set = [i for i in range(1, 10001)]
a = 0
b = 0
for i in range(9999):
    idx = random.randint(0, 9999-i)
    print("? A", set[idx], flush=True)
    n = int(input())
    if n == 1:
        a = set[idx]
        break
    set.remove(set[idx])
if a == 0:
    a = set[0]
set = [i for i in range(1, 10001)]
for i in range(9999):
    idx = random.randint(0, 9999-i)
    print("? B", set[idx], flush=True)
    n = int(input())
    if n == 1:
        b = set[idx]
        break
    set.remove(set[idx])
if b == 0:
    b = set[0]
print("!", a + b)