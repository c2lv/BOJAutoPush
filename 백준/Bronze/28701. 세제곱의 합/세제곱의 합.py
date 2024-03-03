n = int(input())
sum = n*(n+1)//2
square = sum**2
cube = 0
for i in range(1, n+1):
    cube += i**3
print(sum)
print(square)
print(cube)