a, b = map(int, input().split())
c = int(input())

print(a + b) if a + b < 2*c else print(a+b-2*c)