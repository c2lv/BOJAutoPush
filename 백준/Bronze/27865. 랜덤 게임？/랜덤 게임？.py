import sys
input = lambda: sys.stdin.readline().rstrip()

import random

n = int(input())
while True:
    x = random.randint(1, n)
    print('?', x, flush=True)
    answer = input()
    if answer == "Y":
        break
print('!', x, flush=True)
sys.exit()