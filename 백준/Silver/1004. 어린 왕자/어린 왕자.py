t = int(input())
for _ in range(t):
    cnt = 0
    in_same_area = False
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if (x1 - cx)**2 + (y1 - cy)**2 < r**2 and (x2 - cx)**2 + (y2 - cy)**2 < r**2:
            in_same_area = True
        elif (x1 - cx)**2 + (y1 - cy)**2 < r**2 or (x2 - cx)**2 + (y2 - cy)**2 < r**2:
            cnt += 1
    print(cnt)