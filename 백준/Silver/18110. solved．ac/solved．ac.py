import sys
input = lambda: sys.stdin.readline().rstrip()
EPS = 1e-9

n = int(input())
opinion = []
cut = round(n*0.15 + EPS)
avg = 0
for i in range(n):
    opinion.append(int(input()))
opinion.sort()
if n == 0:
    print(0)
else:
    print(round(sum(opinion[cut:n-cut])/(n-2*cut) + EPS))