n, a, b = map(int, input().split())
if a < b or (a >= b and n > b):
    print("Bus")
elif a > b and n <= b:
    print("Subway")
else:
    print("Anything")