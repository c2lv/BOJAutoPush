bottles = list(map(int, input().split()))
total = 0
for bottle in bottles:
    total += bottle
total *= 5
print(total)