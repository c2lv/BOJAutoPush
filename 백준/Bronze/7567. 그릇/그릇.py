import sys

dish = sys.stdin.readline().strip()
recent_dish = ''
height = 0
for i in range(len(dish)):
    if recent_dish == dish[i]:
        height += 5
    else:
        height += 10
    recent_dish = dish[i]
print(height)