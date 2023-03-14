import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [[i, False] for i in queue]
    order = 1
    queue[m][1] = True
    while queue:
        max_important = 0
        for q in queue:
            if q[0] > max_important:
                max_important = q[0]
        while queue[0][0] != max_important:
            queue.append(queue.pop(0))
        d = queue.pop(0)
        if d[1] == True:
            print(order)
        else:
            order += 1