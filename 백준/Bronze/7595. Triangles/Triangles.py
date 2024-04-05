def triangle(n):
    for i in range(n):
        print('*'*(i+1))

while True:
    n = int(input())
    if n == 0:
        break
    triangle(n)