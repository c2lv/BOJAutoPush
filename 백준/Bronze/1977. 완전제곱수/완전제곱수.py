import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(m, n):
    answer = []
    for i in range(m, n + 1):
        if int(i**(1/2))**2 == i:
            answer.append(i)
    print(sum(answer), min(answer), sep='\n') if answer else print(-1)

m = int(input())
n = int(input())
solve(m, n)
