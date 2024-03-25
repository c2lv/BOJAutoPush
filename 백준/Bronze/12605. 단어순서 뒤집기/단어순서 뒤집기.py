import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    word = list(input().split())
    print(f"Case #{i+1}:", *word[::-1])