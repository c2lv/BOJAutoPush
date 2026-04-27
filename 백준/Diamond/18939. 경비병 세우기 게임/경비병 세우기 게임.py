import sys
input = sys.stdin.readline

def solve(n, m, k):
    if m//2+1 <= k or n*m % 2 == 1: # 한방에 끝나거나 칸이 홀수면 유토
        return "Yuto"
    else:
        return "Platina"

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
