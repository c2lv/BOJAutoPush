import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
image1 = []
image2 = []
for _ in range(n):
    image1.append(input())
for _ in range(n):
    image2.append(input())
answer = "Eyfa"
for i in range(n):
    for j in range(2*m):
        if image1[i][j//2] != image2[i][j]:
            answer = "Not Eyfa"
            break
print(answer)