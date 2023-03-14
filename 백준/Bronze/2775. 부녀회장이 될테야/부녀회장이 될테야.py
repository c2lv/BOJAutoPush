import sys
input = sys.stdin.readline

# house[k][n]: k층 n호 거주자 수
house = [None for _ in range(15)]
house[0] = [i for i in range(15)]
for i in range(1, 15):
    house[i] = [sum(house[i - 1][0:j]) for j in range(1, 16)]

# for k in range(1, 15):
#     for n in range(1, 15):
#         print(house[k][n])

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(house[k][n])