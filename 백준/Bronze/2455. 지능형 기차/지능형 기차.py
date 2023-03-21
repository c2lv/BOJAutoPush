import sys
input = sys.stdin.readline

max = 0
passenger = 0
for _ in range(4):
    get_off, get_on = map(int, input().split())
    passenger += get_on - get_off
    if max < passenger:
        max = passenger
print(max)