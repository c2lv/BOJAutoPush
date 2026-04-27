n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

a = 0
for s in size:
    a += s//t + (1 if s%t else 0)
print(a)
print(n//p, n%p)